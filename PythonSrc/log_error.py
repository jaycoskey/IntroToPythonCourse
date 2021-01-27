#!/usr/bin/env python3

from sys import exit, stderr


def log_error(message):
    print('Error: ' + message, file=stderr)
    exit(-1)


if __name__ == '__main__':
    log_error('This is a test')
