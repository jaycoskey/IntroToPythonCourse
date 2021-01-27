#!/usr/bin/env python3

import copy
import sys


# Language features: default function arguments Move.__init__().
# Deep copy
# Slice as copy
# list
# filter
# Line continuation
class Move:
    """Each move records a tranfer of liquids---one of three move_types.

    EMPTY records the complete emptying of one container.
    FILL records the complete filling of one container.
    POUR records the pouring of liquid from one container to another."""
    EMPTY = 0
    FILL = 1
    POUR = 2

    def __init__(self, moveType, jug0, jug1 = 0):
        self.moveType = moveType
        self.jug0 = jug0
        if moveType == Move.POUR:
            assert(jug1 != jug0)
        self.jug1 = jug1  # jug1 is only used for pours

    def __str__(self):
        if self.moveType == Move.EMPTY:
            return 'E{0:d}'.format(self.jug0)
        elif self.moveType == Move.FILL:
            return 'F{0:d}'.format(self.jug0)
        elif self.moveType == Move.POUR:
            return 'P{0:d}->{1:d}'.format(self.jug0, self.jug1)
        else:
            assert(False)


class MoveList:
    def __init__(self):
        self.move_history = []

    def __add__(self, move):
        result = MoveList(self.move_history + move)

    def __getitem__(self, key):
        return self.move_history[key]

    def __iter__(self, move):
        return iter(self.move_history.itervalues())


class Problem:
    def __init__(self, capacities, is_solution):
        self.capacities = capacities
        self.is_solution = is_solution


class Solution:
    def find_solutions(problem):
        num_jugs = len(problem.capacities)
        available_moves = Solution.get_available_moves(num_jugs)
        print('List of moves:')
        for move in available_moves:
            print('  Move: {0:s}'.format(str(move)))
        nohist = []
        ALL_EMPTY = num_jugs * [0]
        partial_nonsolns = [Solution(MoveList(), ALL_EMPTY)]
        solns = []

        is_solution_found = False
        gen_num = 0
        while len(partial_nonsolns) > 0:
            tmp_pnsolns = []
            print( 'Gen #{0:d} has {1:d} partial non-solutions (volumes seen={2:d})'.format(gen_num, len(partial_nonsolns), len(Volumes.seen)))
            gen_num += 1
            for pnsoln in partial_nonsolns:
                for move in available_moves:
                    pnsoln_next = copy.deepcopy(pnsoln).apply_move(move, gen_num)
                    if pnsoln_next == None:
                        continue
                    elif pnsoln_next.volumes.volumes in Volumes.seen:
                        # Found a duplicate
                        continue
                    # We haven't seen this set of volumes before
                    if problem.is_solution(pnsoln_next.volumes.volumes):
                        solns.append(pnsoln_next)
                    else:
                        tmp_pnsolns.append(pnsoln_next)
                        Volumes.seen.append(pnsoln_next.volumes.volumes)
            partial_nonsolns = tmp_pnsolns
        return solns

    def __init__(self, moves, volumes):
        self.moves = moves[:]
        self.volumes = Volumes(volumes[:])

    def __str__(self):
        return '{0:s} @ {1:s}'.format(str(self.volumes), str(self.moves))

    def apply_move(self, move, gen_num):
        if move.moveType == Move.EMPTY:
            if self.volumes[move.jug0] == 0:
                return None
            self.moves.append(str(move))
            self.volumes[move.jug0] = 0
        elif move.moveType == Move.FILL:
            capacity = problem.capacities[move.jug0]
            if self.volumes[move.jug0] == capacity:
                return None
            self.moves.append(str(move))
            self.volumes[move.jug0] = problem.capacities[move.jug0]
        elif move.moveType == Move.POUR:
            src_vol = self.volumes[move.jug0]
            tgt_ullage = problem.capacities[move.jug1] - self.volumes[move.jug1]
            transfer_amount = min(src_vol, tgt_ullage)
            if transfer_amount == 0:
                return None
            self.moves.append(str(move))
            self.volumes[move.jug0] -= transfer_amount
            self.volumes[move.jug1] += transfer_amount
        else:
            assert(False)
        return self

    def get_available_moves(num_jugs):
        available_moves = (
            [Move(Move.EMPTY, j) for j in range(num_jugs)]
            + [Move(Move.FILL, j) for j in range(num_jugs)]
            + [Move(Move.POUR, j, k) for j in range(num_jugs)
                                     for k in range(num_jugs)
                                     if k != j]
            )
        return available_moves

    def get_num_moves(self):
        return len(self.moves)


class Volumes:
    seen = []

    def __init__(self, volumes):
        self.volumes = volumes
        Volumes.seen.append(volumes)

    def __iter__(self):
        return iter(self.volumes)

    def __getitem__(self, key):
        return self.volumes[key]

    def __setitem__(self, key, value):
        self.volumes[key] = value

    def __str__(self):
        return str(self.volumes)

    def seen_str():
        return str(Volumes.seen)


if __name__ == '__main__':
    jug_capacities = [3, 5, 8]
    num_jugs = len(jug_capacities)
    is_solution = lambda vols: vols[2] == 7
    problem = Problem(jug_capacities, is_solution)
    solns = Solution.find_solutions(problem)
    do_show_min_solns = True
    do_show_max_solns = True

    if do_show_min_solns:
        min_moves = -1 if not solns \
                       else min(map(lambda s: s.get_num_moves(), solns))
        is_min_soln = lambda s: s.get_num_moves() == min_moves
        min_solns = list(filter(is_min_soln, solns))

        print('SHORTEST SOLUTIONS ({0:d} moves):'.format(min_moves))
        if min_solns:
            for soln in min_solns:
                print(soln)
        else:
            print('\tNo shortest solutions')

    if do_show_max_solns:
        max_moves = -1 if not solns \
                       else max(map(lambda s: s.get_num_moves(), solns))
        is_max_soln = lambda s: s.get_num_moves() == max_moves
        max_solns = list(filter(is_max_soln, solns))

        print('LONGEST SOLUTIONS ({0:d} moves):'.format(max_moves))
        if max_solns:
            for soln in max_solns:
                print(soln)
        else:
            print('\tNo longest solutions')
