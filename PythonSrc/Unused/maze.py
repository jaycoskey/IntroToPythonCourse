#!/usr/bin/env python3

from collections import namedtuple
import copy
import sys

Candidate = namedtuple('Candidate', ['node', 'path', 'cost'])

# Language features: Slice as copy, list, filter, Line continuation
class Move:
    """Each move is in one of four directions: Up, Down, Left, or Right."""
    U = None
    D = None
    L = None
    R = None

    # mov2str = { U: 'U', D: 'D', L: 'L', R: 'R' }

    def __init__(self, direction):
        # assert(direction in mov2str)
        self.direction = direction

    def __str__(self):
        if self.direction == Move.U.direction:
            return 'U'
        elif self.direction == Move.D.direction:
            return 'D'
        elif self.direction == Move.L.direction:
            return 'L'
        elif self.direction == Move.R.direction:
            return 'R'
        else:
            assert(False)  # Unrecognized Move instance

Move.U = Move(0)
Move.D = Move(1)
Move.L = Move(2)
Move.R = Move(3)

class Problem:
    def __init__(self, maze_filename):
        self.layout = []
        self.start_node = None
        self.finish_node = None
        lines = open(maze_filename).readlines()
        self.num_rows = len(lines)
        self.num_cols = 0
        for row_num in range(0, self.num_rows):
            line = lines[row_num].rstrip()
            self.layout.append(list(line))
            self.num_cols = max(self.num_cols, len(line))
            for col_num in range(0, len(line)):
                if line[col_num].upper() == 'S':
                    self.start_node = (row_num, col_num)
                elif line[col_num].upper() == 'F':
                    self.finish_node = (row_num, col_num)
        self.do_exhaustive_search = True

    def __str__(self):
        return '{0:s} @ {1:s}'.format(str(self.volumes), str(self.moves))

    def apply_move_to_cand(self, cand, move):
        new_node = self.apply_move_to_node(cand.node, move)
        if new_node == None:
            return None
        else:
            new_path = cand.path[::] + [move]  # Is the copy necessary?
            new_cost = cand.cost + 1
            result = Candidate(new_node, new_path, new_cost)
            return result

    def apply_move_to_node(self, node, move):
        """Applies a move (U, D, L, R) to a node (row, col)"""
        assert(self.is_valid(node, move))
        if move == Move.U:
            return (node[0] - 1, node[1])
        elif move == Move.D:
            return (node[0] + 1, node[1])
        elif move == Move.L:
            return (node[0], node[1] - 1)
        elif move == Move.R:
            return (node[0], node[1] + 1)
        else:
            assert(False)  # Unrecognized move

    def char_at(self, node):
        row_num = node[0]
        col_num = node[1]
        return self.layout[row_num][col_num]

    def get_init_cand(self):
        return Candidate(node=self.start_node, path=[], cost=0)

    def get_moves(self, node):
        result = [ move for move in [Move.U, Move.D, Move.L, Move.R]
                   if self.is_valid(node, move) ]
        return result

    def is_open(self, row_num, col_num):
        c = self.layout[row_num][col_num]
        return c == ' ' or c.upper() == 'F'

    def is_soln(self, cand):
        # print('{0:s} == {1:s}'.format(str(cand.node), str(self.finish_node)))
        return cand.node == self.finish_node

    def is_valid(self, node, move, verbose=False):
        """Return True if move is valid from node."""
        row_num = node[0]
        col_num = node[1]
        if move == Move.U:
            result = ( row_num > 0
                       and
                       self.is_open(row_num - 1, col_num) )
            if verbose:
                print('@ {0:s}, {1:s} is {2:s}'.format(str(node), str(move), str(result)))
            return result
        elif move == Move.D:
            result = ( row_num < self.num_rows - 1
                       and
                       self.is_open(row_num + 1, col_num) )
            if verbose:
                print('@ {0:s}, {1:s} is {2:s}'.format(str(node), str(move), str(result)))
            return result
        elif move == Move.L:
            result = ( col_num > 0
                       and
                       self.is_open(row_num, col_num - 1) )
            if verbose:
                print('@ {0:s}, {1:s} is {2:s}'.format(str(node), str(move), str(result)))
            return result
        elif move == Move.R:
            result = ( col_num < self.num_cols - 1
                       and
                       self.is_open(row_num, col_num + 1) )
            if verbose:
                print('@ {0:s}, {1:s} is {2:s}'.format(str(node), str(move), str(result)))
            return result
        else:
            assert(False)  # Unrecognized move

    def mark_path(self, moves):
        cur_node = self.start_node
        for move in moves:
            cur_node =  self.apply_move_to_node(cur_node, move)
            if cur_node != self.finish_node:
                self.set_at(cur_node, 'O')

    def print_maze(self):
        for row_num in range(0, self.num_rows):
            for col_num in range(0, self.num_cols):
                print(self.layout[row_num][col_num], end='')
            print()
        print()

    def set_at(self, node, letter):
        row_num = node[0]
        col_num = node[1]
        typestr = str(type(self.layout[row_num]))
        # print('Type of str.layout[row_num]={0:s}'.format(typestr))
        self.layout[row_num][col_num] = letter


def print_soln(soln):
    print('{0:s} @ [{1:s}]'.format(
        str(soln.node),
        ','.join([str(move) for move in soln.path]),
        soln.cost
        ))


def search_for_solution(problem):
    gen_num = 0
    nodes_seen = []
    solutions = []
    candidates = [problem.get_init_cand()]
    while len(candidates) > 0:
        # print('Gen #{0:d} has {1:d} partial non-soln(s); # seen={2:d}'
        #     .format(gen_num, len(candidates), len(nodes_seen)))
        next_candidates = []
        # print('Gen #{0:d}.  # candidates: {1:d}: {2:s}'
        #     .format(
        #         gen_num,
        #         len(candidates),
        #         ','.join([str(x) for x in candidates])
        #     ))
        for cand in candidates:
            moves = problem.get_moves(cand.node)
            # print('@ {0:s}: # Moves={1:d}: '.format(str(cand.node), len(moves)), end='')
            # for move in moves:
            #     print('{0:s}'.format(str(move)), end='')
            # print()

            avail_moves = [ move for move in moves
                            if problem.apply_move_to_node(cand.node, move)
                                not in nodes_seen ]
            # print('INFO: # AVAIL MOVES={0:d}'.format(len(avail_moves)))
            for next_cand in [ problem.apply_move_to_cand(cand, move)
                               for move in avail_moves ]:
                if next_cand == None:
                    continue
                nodes_seen.append(next_cand.node)
                if problem.is_soln(next_cand):
                    solutions.append(next_cand)
                else:
                    next_candidates.append(next_cand)
        candidates = next_candidates[::]
        if len(solutions) > 0 and not problem.do_exhaustive_search:
            return solutions
        gen_num += 1
    print()
    return solutions


if __name__ == '__main__':
    maze = Problem('winding_maze.txt')
    maze.print_maze()
    solns = search_for_solution(maze)
    print('Number of solutions found: {0:d}'.format(len(solns)))
    soln = solns[0]
    maze.mark_path(soln.path)
    maze.print_maze()

    do_show_min_solns = True
    do_show_max_solns = True

    if do_show_min_solns:
        min_moves = -1 if not solns \
                       else min(map(lambda s: s.cost, solns))
        is_min_soln = lambda s: s.cost == min_moves
        min_solns = list(filter(is_min_soln, solns))

        print('SHORTEST SOLUTIONS ({0:d} moves):'.format(min_moves))
        if min_solns:
            for soln in min_solns:
                print_soln(soln)
        else:
            print('\tNo shortest solutions')
