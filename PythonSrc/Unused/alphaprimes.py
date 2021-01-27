#!/usr/bin/env python3

letters = ['a', 'b', 'c', 'd', 'e']
primes = [2, 3, 5, 7, 11]
letter_ids = range(2, 27)


letters2ids = dict(zip(letters, letter_ids))


def product(items):
    result = 1
    for item in items:
        result *= item
    return result


def str_int(str):
    result = 1
    for letter in str:
        result *= letters2ids[letter]
    return result


if __name__ == '__main__':
    states = { 'Alabama': 'AL', 'Alaska': 'AK', 'Wisconsin': 'WI', 'Wyoming': 'WY' }
    for state_name in states.keys():
        state_code = states[state_name]
        print('State {0:s} has code {1:s}'.format(state_name, state_code))
    for name in states:
        hash_key = product(map(lambda c: ord(c) - ord('a') + 1, name.lower()))
        print('{0:s} -> {1:d}'.format(name, hash_key))
