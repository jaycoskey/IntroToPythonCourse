#!/usr/bin/env python3

import math
import random


def hello_player():
    print("Welcome to Find the Pebble!!  First, pick a board size.")
    print("Then I'll put a pebble at a random spot on the board.")
    print("Then you guess the coordinates of the pebble until you find it.")


def play_loop():
    do_continue_play = True
    while do_continue_play: 
        play_once()
        response = input('Play again (y/n)? ')
        print()
        if response[0].lower() == 'n':
            do_continue_play = False
    print('Bye!')


def play_once():
    board_size = int(input('Pick a board size [2-20]: '))
    print('OK: x & y dimensions range from 1 to {0:d}'.format(board_size))
    is_pebble_found = False
    num_guesses = 0
    while not is_pebble_found:
        pebble_x = random.randrange(1, board_size + 1)
        pebble_y = random.randrange(1, board_size + 1)
        guess = input('Guess the coordinates of the pebble as x,y: ')
        num_guesses += 1
        # The function strip removes extra spaces.
        guess_str_x, guess_str_y = guess.strip().split(',')
        guess_x = int(guess_str_x.strip())
        guess_y = int(guess_str_y.strip())
        if guess_x == pebble_x and guess_y == pebble_y:
            print('You found the pebble in {0:d} guesses!'.format(num_guesses))
            is_pebble_found = True
        else:
            dx = guess_x - pebble_x
            dy = guess_y - pebble_y
            distance = math.sqrt(dx**2 + dy**2)
            print('Your guess ({0:d}, {1:d}) missed the pebble by {2:.2f}'
                    .format(guess_x, guess_y, distance))


if __name__ == '__main__':
    hello_player()
    play_loop()
