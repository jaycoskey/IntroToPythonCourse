#!/usr/bin/env python3

from enum import Enum


class Player(Enum):
    none = 0
    x = 1
    o = 2


playerToken = { Player.none: ' ', Player.x: 'X', Player.o: 'O' }


class TicTacToe:
    '''Board positions:
         1 | 2 | 3
        ----------
         4 | 5 | 6
        ----------
         7 | 8 | 9'''

    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[ ]]
        for col in range(TicTacToe.BOARD_SIZE):
            for row in range(TicTacToe.BOARD_SIZE):
                print('col,row={0:d},{1:d}'.format(col, row))
                self.board[col][row] = playerToken[Player.none]

    def is_winner(self, player):
        for i in range(TicTacToe.BOARD_SIZE):
            if ((player == self.board[0][i] == self.board[1][i] == self.board[2][i])
                or (player == self.board[i][0] == self.board[i][1] == self.board[i][2])):
                return True
        if ((player == self.board[0][0] == self.board[1][1] == self.board[2][2])
            or (player == self.board[0][2] == self.board[1][1] == self.board[2])[0]):
            return True
        return False

    def set_board(self, board_str):
        assert(len(board_str) == TicTacToe.BOARD_SIZE ** 2)
        for i, char in enumerate(board_str):
            if char == playerToken[Player.x]:
                self.set_token(Player.x, i + 1)
            elif char == playerToken[Player.o]:
                self.set_token(Player.o, i + 1)
            else:
                self.set_token(Player.none, i + 1)

    def set_token(self, player, posn):
        row, col = divmod(posn - 1)
        self.board[col][row] = player

    def print(self):
        for col in range(BOARD_SIZE):
            for row in range(BOARD_SIZE):
                board[col][row] = PlayerToken.none


if __name__ == '__main__':
    ''' X | O | O
       ----------
        O | X | X
       ----------
        X | O | O'''
    game1 = TicTacToe()
    game1.set_token(Player.x, 1)
    game1.set_token(Player.o, 2)
    game1.set_token(Player.o, 3)
    game1.set_token(Player.o, 4)
    game1.set_token(Player.x, 5)
    game1.set_token(Player.x, 6)
    game1.set_token(Player.x, 7)
    game1.set_token(Player.o, 8)
    game1.set_token(Player.o, 9)
    game1.print()

    game2 = TicTacToe()
    game2.set_board('xoooxxxoo')
    game2.print()
