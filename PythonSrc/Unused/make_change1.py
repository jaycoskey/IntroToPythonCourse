#!/usr/bin/env python3

coins = [1, 5, 10, 25, 50]

def get_ways_to_make_change(n):
    assert(n >= 0)
    solutions = [[] for k in range(n + 1)]
    solutions[0] = [[]]  # Base case
    for k in range(n + 1):  # For each monetary amount
        for coin in coins:
            if coin <= k:
                for soln in solutions[k - coin]:
                    solutions[k].append(soln + [coin])
    # for k in range(n + 1):
    #     print(k, ': ', solutions[k])
    return solutions[n]


if __name__ == '__main__':
    solutions = get_ways_to_make_change(25)
    for soln in solutions:
        print(soln)
