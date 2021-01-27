#!/usr/bin/env python3

NONE = 0
ROCK = 1
PAPER = 2
SCISSORS = 3


def rps_assert(rps_f):
    assert(rps_f(PAPER, PAPER) == NONE)
    assert(rps_f(PAPER, ROCK) == PAPER)
    assert(rps_f(PAPER, SCISSORS) == SCISSORS)

    assert(rps_f(ROCK, PAPER) == PAPER)
    assert(rps_f(ROCK, ROCK) == NONE)
    assert(rps_f(ROCK, SCISSORS) == ROCK)

    assert(rps_f(SCISSORS, PAPER) == SCISSORS)
    assert(rps_f(SCISSORS, ROCK) == ROCK)
    assert(rps_f(SCISSORS, SCISSORS) == NONE)


def rps_winner_by_result(a, b):
    if a == b:
        return NONE
    elif a == ROCK and b == PAPER or a == PAPER and b == ROCK:
        return PAPER
    elif a == ROCK and b == SCISSORS or a == SCISSORS and b == ROCK:
        return ROCK
    elif a == PAPER and b == SCISSORS or a == SCISSORS and b == PAPER:
        return SCISSORS
    else:
        print('Not Possible')


def rps_winner_flip(a, b):
    if a == b:
        return NONE
    elif a == PAPER and b == ROCK:
        return PAPER
    elif a == ROCK and b == SCISSORS:
        return ROCK
    elif a == SCISSORS and b == PAPER:
        return SCISSORS
    else:
        return rps_winner_flip(b, a)


def rps_winner(a, b):
    if a == b:
        return NONE
    elif a == PAPER and b == ROCK:
        return PAPER
    elif a == ROCK and b == SCISSORS:
        return ROCK
    elif a == SCISSORS and b == PAPER:
        return SCISSORS
    elif a == ROCK and b == PAPER:
        return PAPER
    elif a == SCISSORS and b == ROCK:
        return ROCK
    elif a == PAPER and b == SCISSORS:
        return SCISSORS


def rps_winner_exhaustive(a, b):
    if a == PAPER and b == PAPER:
        return NONE
    elif a == ROCK and b == ROCK:
        return NONE
    elif a == SCISSORS and b == SCISSORS:
        return NONE
    elif a == PAPER and b == ROCK:
        return PAPER
    elif a == ROCK and b == SCISSORS:
        return ROCK
    elif a == SCISSORS and b == PAPER:
        return SCISSORS
    elif a == ROCK and b == PAPER:
        return PAPER
    elif a == SCISSORS and b == ROCK:
        return ROCK
    elif a == PAPER and b == SCISSORS:
        return SCISSORS


def rps_winner_misc(a, b):
    if a == b:
        return NONE
    elif (a == PAPER and b == ROCK) or (a == ROCK and b == PAPER):
        return PAPER
    elif (a == ROCK and b == SCISSORS) or (a == SCISSORS and b == ROCK):
        return ROCK
    elif (a == PAPER and b == SCISSORS) or (a == SCISSORS and b == PAPER):
        return SCISSORS


def test():
    rps_assert(rps_winner_by_result)
    rps_assert(rps_winner_flip)
    rps_assert(rps_winner)
    rps_assert(rps_winner_exhaustive)
    rps_assert(rps_winner_misc)

test()
