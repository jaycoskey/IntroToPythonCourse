#!/usr/bin/env python3

MIN_LENGTH = 4
WORDLIST = 'wordlist.txt'


if __name__ == '__main__':
    words = {line.rstrip(): 1 for line in open(WORDLIST).readlines()}
    for word in words.keys():
        if len(word) < MIN_LENGTH:
            continue
        # print('Word={0:s}'.format(word))
        is_paninitial = True
        for i in range(2, len(word)):
            subword = word[i: len(word)]
            if subword not in words:
                # print('Not a word:', subword)
                is_paninitial = False
                break
        if is_paninitial:
            print(word)
