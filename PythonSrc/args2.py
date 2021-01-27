#!/usr/bin/env python3

from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        print('More than one argument')
    for i in range(1, len(argv)):
        print(argv[i])
