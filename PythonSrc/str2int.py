#!/usr/bin/env python3

from functools import reduce


char2int = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }


def str2int(s):
    s2i = lambda acc, char: 10 * acc + char2int[char]
    return reduce(s2i, s, 0)


def sum(items):
    return reduce(lambda acc, x: acc + x, items, 0)


def product(items):
    return reduce(lambda acc, x: acc * x, items, 1)


if __name__ == '__main__':
    print(str2int('861357492'))
    print(product([1,2,3,4,5]))
