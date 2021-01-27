#!/usr/bin/env python3

from collections import Counter


FILEPATH = 'wordlist.txt'


word2counter = dict()  # Create an empty dictionary
for word in open(FILEPATH).readlines():
    word = word.rstrip()  # Remove extra space from end of string
    word2counter[word] = Counter(word)


for w1 in word2counter.keys():
    for w2 in word2counter.keys():
        if w2 == w1:
            continue
        if word2counter[w1] == word2counter[w2]:
            print('Found a pair: {0:s}, {1:s}'.format(w1, w2))
