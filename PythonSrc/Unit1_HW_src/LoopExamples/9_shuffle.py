#!/usr/bin/python3

from random import randint


def shuffle(items):
    max_ind = len(items) - 1
    while max_ind > 0:
        rnd_ind = randint(0, max_ind)
        if rnd_ind != max_ind:
            items[rnd_ind], items[max_ind] = items[max_ind], items[rnd_ind]
        max_ind -= 1 
    return items


if __name__ == '__main__':
    unshuffled = list(range(0, 5))
    print(unshuffled)
    shuffled = shuffle(unshuffled[:])
    print(shuffled)

    # for i in range(1, len(sys.argv)):
    #     print(sys.argv[i])
