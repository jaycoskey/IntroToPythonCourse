#!/usr/bin/env python3

from random import randint


values    = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K' ]
suits     = [ 'C', 'D', 'H', 'S' ]
deck      = [ (value, suit) for value in values for suit in suits ]
positions = [ randint(0, 51) for k in range(0, 7) ]
cards     = list(map(lambda pos: deck[pos], positions))


to_value = lambda c: c[0]
to_suit  = lambda c: c[1]
def print_card(c):
    print('{0:s} of {1:s}'.format(c[0], c[1]))


for c in cards:
    print('{0:s} of {1:s}'.format(c[0], c[1]))
print('=====')
for spade_card in filter(lambda c: to_suit(c) == 'S', cards):
    print_card(spade_card)
print('=====')
for v in map(to_value, cards):
    print('Values: {0:s}'.format(v))
print('=====')
for s in map(to_suit, cards):
    print('Suit: {0:s}'.format(s))
