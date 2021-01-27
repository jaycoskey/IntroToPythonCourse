#!/usr/bin/env python3

from functools import reduce

def red(f, items, x0):
    if items == []:
        return x0
    else:
        return red(f, items[1:], f(x0, items[0]))

def sm(items):
    return red(lambda acc,x: acc + x, items, 0)

def prod(items):
    return red(lambda acc,x: acc * x, items, 1)

def stringify(ints):
    return reduce(lambda s,k: s + ('q'*k), ints, '')

# print(sm([1,2,3,4,5]))
# print(prod([1,2,3,4,5]))
print(stringify([1,2,3,4,5]))
