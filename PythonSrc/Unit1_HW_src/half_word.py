#!/usr/bin/env python3

def print_half_word(word):
    for i in range(0, len(word)):
        if i % 2 == 0:
            print(word[i], end='')
    print()


print_half_word('ions')
print_half_word('pulsations')
print_half_word('slingshots')
