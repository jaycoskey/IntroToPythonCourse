#!/usr/bin/env python3

def replace(items, f):
    return [f(x) for x in items]


if __name__ == '__main__':
    items = [1,2,3,4,5]
    square = lambda x: x**2
    print(replace(items, square))
