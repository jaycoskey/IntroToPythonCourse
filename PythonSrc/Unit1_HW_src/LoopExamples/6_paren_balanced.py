#!/usr/bin/python3

import sys


# Homework:
#   Write a function called paren_validate that takes one string argument,
#   and prints out either
#     (a) Valid: [str]
#     (b) Error: Extra right-parenthesis
#     (c) Error: Missing right-parenthesis
#   In cases (b) and (c), also print out the string argument on the next line,
#   with a caret pointing out the location of the problem on the line after that.
#   Example #1
#           Error: Extra right-parenthesis
#               ( a ) b ) c )
#                   ^
#
#   Example #2
#           Error: Missing right-parenthesis
#               ( a ( b )
#                        ^
#


def is_paren_balanced(str):
    # '''TODO: Implement algorithm'''
    paren_depth = 0
    for c in str:
        if c == '(':
            paren_depth += 1
        elif c == ')':
            if paren_depth < 0:
                return False
            else:
                paren_depth -= 1
        else:
            pass
    return paren_depth == 0


def paren_test(str):
    is_balanced = is_paren_balanced(str)
    print('Str="{0:s}"; Balanced="{1}"'.format(str, is_balanced))


def main():
    paren_test('( a ( b ) c )')
    paren_test('( a ) b ) c )')
    paren_test('( a ( b )')


if __name__ == '__main__':
    main()
