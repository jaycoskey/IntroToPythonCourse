#!/usr/bin/env python3

from collections import Counter


MIN_LENGTH = 13
WORDLIST = 'wordlist.txt'
for line in open(WORDLIST).readlines():
    line = line.rstrip()
    cntr = Counter(line)
    if max(cntr.values()) == 1 and len(line) >= MIN_LENGTH:
        print(line)
