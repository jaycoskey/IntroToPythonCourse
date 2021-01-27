#!/usr/bin/env python3

def count_palindromes(a, b):
    count = 0
    for i in range(a, b):
        s = str(i)
        if s == s[::-1]:
            count += 1
    return count


print('# of palindromes = {0:d}'.format(count_palindromes(10, 1000000)))
