#!/usr/bin/env python3

def maxmin(a, b, x):
    return max(a, min(b, x))


if __name__ == '__main__':
    print(maxmin(0, 10, -5))
    print(maxmin(0, 10,  0))
    print(maxmin(0, 10,  5))
    print(maxmin(0, 10, 10))
    print(maxmin(0, 10, 15))
