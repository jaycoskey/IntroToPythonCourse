#!/usr/bin/env python3

from collections import Counter


def ecount1(s):
    cntr = Counter(s)
    return cntr['e']


def ecount2(s):
    count = 0
    for letter in s:
        if letter == 'e':
            count += 1
    return count


s = 'masslessness'
print(ecount1(s))
print(ecount2(s))
