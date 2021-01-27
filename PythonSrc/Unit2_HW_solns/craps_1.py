#!/usr/bin/env python3

from enum import Enum
from random import randint


LOSE = 0
WIN = 1


def get_roll_sum(n = 2):
    """Returns the sum of the rolls of n six-sided dice."""
    faces = 6
    # Note: randint(a, b) generates a random number x for which a <= x <= b.
    #       In other words, the possible range includes both the arguments.
    dice_values = [randint(1, faces) for k in range(0, n)]
    return sum(dice_values)


def get_round_outcome():
    """Returns the outcome of one round of craps.

    The result is either LOSE or WIN."""
    first_roll_sum = get_roll_sum() 
    if first_roll_sum in [2, 3, 12]:
        return LOSE
    elif first_roll_sum in [7, 11]:
        return WIN
    else:
        point = first_roll_sum
        while True:
            roll = get_roll_sum(2)
            if roll == 7:
                return LOSE
            elif roll == point:
                return WIN


def play_set(num_rounds):
    """Returns an ordered pair (wins, losses) after n rounds of craps."""
    losses = 0
    wins = 0
    for round_num in range(num_rounds):
        if round_num % 1000 == 0:
            print('.', end='', flush=True)
        outcome = get_round_outcome()
        if outcome == LOSE:
            losses += 1
        else:
            wins += 1
    print('.')
    return (wins, losses)


def test_rolls():
    rolls = [get_roll_sum() for k in range(0, 1000)]
    assert(min(rolls) == 2)
    assert(max(rolls) == 12)
    average = sum(rolls) / len(rolls)
    assert(average > 6 and average < 8)


if __name__ == '__main__':
    test_rolls()
    rounds = 10000
    (wins, losses) = play_set(rounds)
    print('Rounds played={0:,d}.  Won {1:.2f}%; Lost {2:.2f}%'
        .format(rounds, 100*wins/rounds, 100*losses/rounds))
