#!/usr/bin/env python3

import sys


def infinite_recursion():
    return infinite_recursion()


if __name__ == '__main__':
    print(sys.version)
    infinite_recursion()
