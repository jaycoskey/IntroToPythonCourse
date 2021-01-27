#!/usr/bin/env python3

from collections import Counter


def print_char_count(word):
    cntr = Counter(word.lower())
    print(cntr)


print_char_count('abcdABCD')    
print_char_count('aabbCCDD')    
print_char_count('masslessness')    
