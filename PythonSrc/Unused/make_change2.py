#!/usr/bin/env python3

from collections import Counter

coins = [1, 5, 10, 25, 50]

def add_coin(soln, coin):
    assert(str(type(soln)) == "<class 'collections.Counter'>")
    result = soln.copy()
    if coin in result:
        result[coin] += 1
    else:
        result[coin] = 1
    return result

def get_ways_to_make_change(n):
    assert(n >= 0)
    solutions = [[] for k in range(n + 1)]
    solutions[1] = [Counter({1: 1})]  # Base case
    for k in range(2, n + 1):  # For each monetary amount
        for coin in coins:
            if coin < k:
                for soln in solutions[k - coin]:
                    newsoln = add_coin(soln, coin)
                    assert(solution_sum(newsoln) == k)
                    solutions[k].append(newsoln)
            elif coin == k:
                solutions[k].append(Counter({coin:1}))
    # for k in range(n + 1):
    #     for soln in solutions[k]:
    #         print(k, ': ', solution_str(soln))
    return solutions[n]

def solution_str(soln):
    result = ''
    for k in soln.keys():
        result += str(k) + ':' + str(soln[k]) + ';'
    return result

def solution_sum(soln):
    result = 0
    for elem in soln.elements():
        result += elem
    return result


if __name__ == '__main__':
    n = 10
    solutions = get_ways_to_make_change(n)
    print('Printing results for n={0:d}'.format(n))
    for soln in solutions:
        print('n={0:d}: soln={1:s}'.format(n, solution_str(soln)))
