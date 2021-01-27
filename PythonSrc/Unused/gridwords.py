#!/usr/bin/env python3

import sys

WORDLIST = '/usr/share/dict/words'
MIN_WORD_LENGTH = 8
MAX_WORD_LENGTH = 50

class Poslet:
    '''x,y position of letter in grid, together with the letter itself'''
    def __init__(self, row, col, letter):
        self.row = row
        self.col = col
        self.letter = letter

def get_dlinks(rows, r, c):
    return [
             ( Poslet(r,     c,     rows[r]    [c]),
               Poslet(r + 1, c + 1, rows[r + 1][c + 1]) ),
             ( Poslet(r,     c + 1, rows[r]    [c + 1]),
               Poslet(r + 1, c,     rows[r + 1][c]) )
           ]

def get_words(wordfile):
   with open(wordfile, 'r') as f:
       words = [word.strip() for word in f.readlines()]
   return words

def is_word_in_links(poslets, links, word):
    cur_poslets = [poslet for poslet in poslets
                   if poslet.letter == word[0]]
    for i in range(1, len(word)):
        next_poslets = []
        for cur_poslet in cur_poslets:
            for link in links:
                oldRow  = link[0].row
                oldCol  = link[0].col
                # oldChar = link[0].letter
                # newRow  = link[1].row
                # newCol  = link[1].col
                newChar = link[1].letter
                if (newChar == word[i]
                    and cur_poslet.row == oldRow
                    and cur_poslet.col == oldCol):
                        next_poslets.append(link[1])
        cur_poslets = next_poslets
    return True if cur_poslets else False

def reversed_links(links):
    return [(poslet2, poslet1) for (poslet1, poslet2) in links]

if __name__ == '__main__':
    rows = [['n', 'o', 'r', 't'],
            ['h', 'w', 'e', 's'],
            ['t', 'y', 'e', 's'],
            ['h', 'i', 'v', 'a']]
    poslets = [Poslet(r, c, rows[r][c])
                 for r in range(0, 4) for c in range(0, 4)]
    hlinks = [(Poslet(r, c, rows[r][c]), Poslet(r, c+1, rows[r][c + 1]))
                 for r in range(0, 4) for c in range(0, 3)]
    vlinks = [(Poslet(r, c, rows[r][c]), Poslet(r+1, c, rows[r+1][c]))
                 for r in range(0, 3) for c in range(0, 4)]
    dlinks00 = get_dlinks(rows, 0, 0)
    dlinks02 = get_dlinks(rows, 0, 2)
    dlinks20 = get_dlinks(rows, 2, 0)
    dlinks22 = get_dlinks(rows, 2, 2)

    prelinks = hlinks + vlinks + dlinks00 + dlinks02 + dlinks20 + dlinks22
    links = prelinks + reversed_links(prelinks)  # Bi-directional links
    links = list(set(links))                     # De-duped
    words = get_words(WORDLIST)
    found_words = [word for word in words
                      if is_word_in_links(poslets, links, word)
                      and len(word) >= MIN_WORD_LENGTH
                      and len(word) <= MAX_WORD_LENGTH
                  ]
    for word in found_words:
        print(word)
