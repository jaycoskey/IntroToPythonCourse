#!/usr/bin/env python3

# Homework:
#   (a) Ensure both board printouts to match.
#   (b) Modify the __init__() function so that it takes an optional string argument
#       that matches the layout of the board, just as the string argument to set_board() does.
#   (c) Add a function called test() that creates 3+8 = 11 games
#        * draw1: The board is empty
#        * draw2: The board is partially full, and neither player wins.
#        * draw3: The board is full, and neither player wins.
#       The "win games" cover the 8 way (3 rows, 3 cols, 2 diags) a single player can win.
#       They should have all their cells filled in.
#       When each test is written, either player can be chosen to be the winner.
#        * win1, win2, win3: One of the players wins, with a horizontal 3-in-a-row.
#        * win4, win5, win6: One of the players wins, with a vertical 3-in-a-row.
#        * win7, win8:       One of the players wins, with a diagonal 3-in-a-row.
#   (d) For each game in (c), add an assert statement to validate that get_winner() returns the correct value.
#   (e) Have the __main__ portion of the script call test.
#   (f) Fix any bugs found along the way.
# 
from enum import Enum

class Player(Enum):
    noone = 0
    x = 1
    o = 2

playerToken = { Player.noone: ' ', Player.x: 'X', Player.o: 'O' }

class Game:
    '''Board positions:
         1 | 2 | 3
        ----------
         4 | 5 | 6
        ----------
         7 | 8 | 9'''

    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[playerToken[Player.noone]
            for col in range(Game.BOARD_SIZE)]
            for row in range(Game.BOARD_SIZE)]
        # for row in range(Game.BOARD_SIZE):
        #     for col in range(Game.BOARD_SIZE):
        #         print('row,col={0:d},{1:d}'.format(row, col))
        #         self.board[row][col] = playerToken[Player.noone]

    def get_winner(self):
        if self.is_winner(Player.x):
            return Player.x
        elif self.is_winner(Player.o):
            return Player.o
        else:
            return Player.noone

    def is_winner(self, player):
        for i in range(Game.BOARD_SIZE):
            # Check for a win (3-in-a-row) that's a column ~or~ a row.
            if ((player == self.board[0][i] == self.board[1][i] == self.board[2][i])
                or (player == self.board[i][0] == self.board[i][1] == self.board[i][2])):
                return True
        # Check for a win that's a diagonal.
        if ((player == self.board[0][0] == self.board[1][1] == self.board[2][2])
            or (player == self.board[0][2] == self.board[1][1] == self.board[2][0])):
            return True
        return False

    def set_board(self, board_str):
        assert(len(board_str) == Game.BOARD_SIZE ** 2)
        for i, char in enumerate(board_str):
            # print('DEBUG: char={0:s}'.format(char))
            if char == playerToken[Player.x]:
                self.set_token(Player.x, i + 1)
            elif char == playerToken[Player.o]:
                self.set_token(Player.o, i + 1)
            else:
                self.set_token(Player.noone, i + 1)

    def set_token(self, player, posn):
        row, col = divmod(posn - 1, Game.BOARD_SIZE)
        self.board[row][col] = playerToken[player]

    def print(self):
        hseparator = '---' + ('+---' * (Game.BOARD_SIZE - 1)) + '\n'
        hsep = ''
        for row in range(Game.BOARD_SIZE):
            print(hsep, end='')
            hsep = hseparator  # Set to non-noone after first iteration
            vseparator = '|'
            vsep = ''
            for col in range(Game.BOARD_SIZE):
                print(vsep, end='')
                vsep = vseparator  # Set to non-noone after first iteration
                print(' {0:s} '.format(self.board[row][col]), end='')
            print('')

    def print_winner(self):
        winner = self.get_winner()
        if winner == Player.x:
            print('Player X won!!')
        elif winner == Player.o:
            print('Player O won!!')
        else:
            print('Neither player has won.')


def info_print_tokens():
    print('Player tokens: <<{0:s}>>, <<{1:s}>>, <<{2:s}>>'.format(
        playerToken[Player.noone], playerToken[Player.x], playerToken[Player.o]))

if __name__ == '__main__':
    '''game1 test case:
        X | O | O
       ---+---+---
        O | X | X
       ---+---+--
        X | O | O'''

    # info_print_tokens()

    game1 = Game()
    game1.set_token(Player.x, 1)
    game1.set_token(Player.o, 2)
    game1.set_token(Player.o, 3)
    game1.set_token(Player.o, 4)
    game1.set_token(Player.x, 5)
    game1.set_token(Player.x, 6)
    game1.set_token(Player.x, 7)
    game1.set_token(Player.o, 8)
    game1.set_token(Player.o, 9)
    game1.print()  # Should match docstring, above.
    print('')
    game1.print_winner()

    print('\n\n\n')
    game2 = Game()
    game2.set_board('XOOOXXXOO')
    game2.print()  # Should match game1.
    print('')
    game2.print_winner()

    print('\n\n\n')
    game3 = Game()
    game3.set_board('XXXOXOXOO')
    game3.print()  # Should match game1.
    print('')
    game3.print_winner()
