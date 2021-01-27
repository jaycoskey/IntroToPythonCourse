#!/usr/bin/env python3

# import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('More than one argument')
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
