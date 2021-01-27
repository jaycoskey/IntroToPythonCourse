#!/usr/bin/env python3

from collections import Counter
from random import randint
# Note: The range of randint(a, b) is inclusive.
#       For randrange(x, y) it is exclusive at the end.
#       Thus randint(a, b) = randrange(a, b + 1)

MIN_PEOPLE = 2
MAX_PEOPLE = 50
TRIAL_COUNT = 10
MIN_MULTIPLICITY = 2

def get_birthday_success_count(num_people, num_trials, min_multiplicity):
    result = 0
    for num_trial in range(0, TRIAL_COUNT):
        birthdays = [ randint(1, 365) for k in range(0, num_people) ]
        counts = Counter(birthdays)
        is_shared_birthday = max(counts.values()) >= MIN_MULTIPLICITY
        if is_shared_birthday:
            result += 1
    return result


def get_birthday_info(min_people, max_people, num_trials, min_multiplicity):
    for num_people in range(min_people, max_people + 1):
        success_count = get_birthday_success_count(
                num_people, num_trials, min_multiplicity)
        yield (num_people, (success_count, num_trials))


def main():
    birthday_dict = dict((n, 100 * s/t)
            for (n, (s,t))
            in get_birthday_info(
                MIN_PEOPLE, MAX_PEOPLE + 1, TRIAL_COUNT, MIN_MULTIPLICITY))
    for n in birthday_dict:
        print('People: {0:3d}; Shared birthday count >= {1:d}: {2: >8.4f}%'
            .format(n, MIN_MULTIPLICITY, birthday_dict[n]))


if __name__ == '__main__':
    main()  # TODO: Pass any future arguments from the command line.
