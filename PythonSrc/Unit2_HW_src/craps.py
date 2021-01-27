#!/usr/bin/env python3

from enum import Enum
from random import randint


LOSE = 0
WIN = 1


def get_roll_sum():
    """Returns the sum of the rolls of two six-sided dice."""
    faces = 6
    n = 2
    # Note: randint(a, b) generates a random number x for which a <= x <= b.
    #       So the possible range includes both the arguments.
    dice_values = [randint(1, faces) for k in range(0, n)]
    return sum(dice_values)


def get_round_outcome():
    """Returns the outcome of one round of craps, returning WIN or LOSE."""
    return LOSE  # TODO: REPLACE THIS LINE WITH CODE THAT PLAYS OUT A ROUND.


def play_set(num_rounds):
    """Returns an ordered pair (wins, losses) after n rounds of craps."""
    losses = 0
    wins = 0
    for round_num in range(num_rounds):
        if round_num % 1000 == 0:
            print('.', end='', flush=True)  # Flush means print it right now.
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
