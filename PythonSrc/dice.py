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
    roll_count = 5000
    probability = [0, 0,
            1/36, 2/36, 3/36, 4/36, 5/36,
            6/36,
            5/36, 4/36, 3/36, 2/36, 1/36
            ]
    roll_record = {}
    for i in range(roll_count):
        roll = d6_roll(2)
        if roll in roll_record:
            roll_record[roll] += 1
        else:
            roll_record[roll] = 1
    for r in range(2, 13):
        print('Roll={0:d}: {1:d} times out of {2:d} = {3:.2f}% (vs. prob = {4:.2f}%)'
                .format(r, 
                    roll_record[r],
                    roll_count, 100 * roll_record[r] / roll_count,
                    100 * probability[r])
                    )
