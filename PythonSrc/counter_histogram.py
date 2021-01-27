#!/usr/bin/env python3

from collections import Counter


def print1(cntr):
    for letter in cntr.keys():
        print('{0:s}: {1:s}'.format(letter, '#' * cntr[letter]))


def print2(cntr):
    for letter in sorted(cntr, key=cntr.get):
        print('{0:s}: {1:s}'.format(letter, '#' * cntr[letter]))


if __name__ == '__main__':
    # word = 'supercalifragilisticexpialidocious'
    word = 'indivisibilities'
    cntr = Counter(word)
    print1(cntr)
    # print2(cntr)
