#!/usr/bin/env python3

def print_list_v1(items):
    print('[', end='')
    for i in range(0, len(items)):
        if i > 0:
            print(', ', end='')
        print(items[i], end='')
    print(']')


def print_list_v2(items):
    sep = ''  # separator
    print('[', end='')
    for i in range(0, len(items)):
        print('{0:s}{1:s}'.format(sep, items[i]), end='')
        sep = ', '
    print(']')


print_list_v1('abcdefghij')
print_list_v2('abcdefghij')
