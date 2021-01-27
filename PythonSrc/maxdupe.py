#!/usr/bin/env python3

from collections import Counter


MINDUPES = 7
WORDLIST = 'wordlist.txt'
for line in open(WORDLIST).readlines():
    line = line.rstrip()
    cntr = Counter(line)
    if max(cntr.values()) >= MINDUPES:
        print(line)
