#!/usr/bin/env python3

from functools import reduce

def all_loop(items):
    for b in items:
        if not b:
            return False
    return True

def any_loop(items):
    for b in items:
        if b:
            return True
    return False

def all_reduce(items):
    return reduce(lambda acc,b: acc and b, items, True)

def any_reduce(items):
    return reduce(lambda acc,b: acc or b, items, False)

def test_equal(items):
    print('all_loop({0:s}) = {1:s}'.format(str(items), str(all_loop(items))))
    print('any_loop({0:s}) = {1:s}'.format(str(items), str(any_loop(items))))
    assert(all_loop(items) == all_reduce(items))
    assert(any_loop(items) == any_reduce(items))

if __name__ == '__main__':
    EMPTY = []

    SINGLE_FALSE = [False]
    MULTI_FALSE = [False, False]

    SINGLE_TRUE = [True]
    MULTI_TRUE = [True, True]

    FALSE_TRUE = [False, True]

    test_equal(EMPTY)
    test_equal(SINGLE_FALSE)
    test_equal(MULTI_FALSE)
    test_equal(SINGLE_TRUE)
    test_equal(MULTI_TRUE)
    test_equal(FALSE_TRUE)
