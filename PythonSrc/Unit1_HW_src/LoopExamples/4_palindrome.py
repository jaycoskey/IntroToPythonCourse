#!/usr/bin/env python3

MIN_LENGTH = 2
# WORDLIST = 'wordlist.txt'
WORDLIST = 'wordlist_short.txt'


def is_palindrome_v1(word):
    return word[::] == word[::-1]

    
def is_palindrome_v2(word):
    first = 0
    last = len(word) - 1
    while (first < last):
        if word[first] != word[last]:
            return False
        first += 1
        last -= 1
    return True

    
if __name__ == '__main__':
    lines = open(WORDLIST).readlines()
    for line in lines:
        line = line.rstrip()
        if is_palindrome_v12(line) and len(line) >= MIN_LENGTH:
            print(line)
