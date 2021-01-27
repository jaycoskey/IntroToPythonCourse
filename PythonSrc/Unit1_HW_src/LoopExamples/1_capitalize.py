#!/usr/bin/env python3

def print_with_capitalized_a(word):
    for letter in word:
        if letter == 'a':
            print(letter.upper(), end='')
        else:
            print(letter, end='')


def print_with_capitalized_ends(word):
    for i in range(0, len(word)):
        letter = word[i]
        if i == 0 or i == len(word) - 1:
            print(letter.upper(), end='')
        else:
            print(letter, end='')
    print()


print_with_capitalized_a('baaag')print_with_capitalized_ends('baaag')
