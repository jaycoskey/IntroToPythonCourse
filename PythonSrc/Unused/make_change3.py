#!/usr/bin/env python3

from collections import Counter


def add_coin(soln, coin):
    # assert(str(type(soln)) == "<class 'collections.Counter'>")
    assert(type(soln).__name__ == 'Counter')
    result = soln.copy()
    if coin in result:
        result[coin] += 1
    else:
        result[coin] = 1
    return result


def get_ways_to_make_change(n, coins):
    assert(n >= 0)
    solutions = [[] for k in range(n + 1)]
    solutions[1] = [Counter({1: 1})]  # Base case
    for k in range(2, n + 1):  # For each monetary amount
        for coin in coins:
            if coin < k:
                for soln in solutions[k - coin]:
                    newsoln = add_coin(soln, coin)
                    assert(solution_sum(newsoln) == k)
                    if not newsoln in solutions[k]:
                        solutions[k].append(newsoln)
            elif coin == k:
                solutions[k].append(Counter({coin:1}))
    return solutions[n]


def solution_str(soln):
    def denomination_str(k): return '{0:d}:{1:d}'.format(k, soln[k])
    result = '; '.join([denomination_str(k) for k in soln.keys()])
    return result


def solution_sum(soln):
    return sum([elem for elem in soln.elements()])


if __name__ == '__main__':
    n = 25
    coins = [1, 5, 10, 25, 50]
    solutions = get_ways_to_make_change(n, coins)
    print('Printing results for n={0:d}'.format(n))
    for soln in solutions:
        print('n={0:d}: soln={1:s}'.format(n, solution_str(soln)))
