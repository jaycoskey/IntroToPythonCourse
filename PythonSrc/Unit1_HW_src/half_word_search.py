#!/usr/bin/env python3

MIN_LENGTH = 10
WORDLIST = 'wordlist.txt'


if __name__ == '__main__':
    whole_words = {line.rstrip(): 1 for line in open(WORDLIST).readlines()}
    for word in whole_words.keys():
        half_word = ''.join([word[k] for k in range(0, len(word)) if k % 2 == 0])
        # if len(word) >= MIN_LENGTH and half_word in whole_words:
        if half_word == 'in':
            print('{0:s} -> {1:s}'.format(word, half_word))
