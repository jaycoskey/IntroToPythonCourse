#!/usr/bin/env python3

from enum import Enum
from random import randint
# Note: The range of randint(a, b) is inclusive.
#       For randrange(x, y) it is exclusive at the end.
#       Thus randint(a, b) = randrange(a, b + 1)


class Outcome(Enum):
    win = 1
    lose = 2


def d6_roll(n = 1):
    return die_roll(6, n)


def die_roll(sides = 6, n = 1):
    dice_values = [randint(1, sides) for k in range(0, n)]
    # print(dice_values)
    return sum(dice_values)


if __name__ == '__main__':
    init_funds = 5000
    funds = init_funds
    rounds = 5000
    wager = 1
    for i in range(rounds):
        # print(i, end='', flush=True)
        come_out_roll = d6_roll(2) 
        if come_out_roll in [2, 3, 12]:
            funds -= wager
            continue
        elif come_out_roll in [7, 11]:
            funds += wager
            continue
        else:
            point = come_out_roll
            print('Point={0:d} ... '.format(point), end='')
            while True:
                roll = d6_roll(2)
                if (roll == 7):
                    print('Player lost on {0:d} != {1:d}'.format(roll, point))
                    funds -= wager
                    break
                elif (roll == point):
                    print('Player won on {0:d} !!!!'.format(roll))
                    funds += wager
                    break
    print('Player started with ${0:,d} and bet $1 on each of {1:,d} rounds.  Ended up with ${2:,d}.'
            .format(init_funds, rounds, funds))
