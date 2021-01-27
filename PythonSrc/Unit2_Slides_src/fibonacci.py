#!/usr/bin/env python3

import timeit


class Fibonacci:
    def __init__(self):
        pass

    def fibonacci(self, n):
        assert(type(n) == int and n >= 0)
        if n == 0 or n == 1:
            return 1
        else:
            return self.fibonacci(n - 2) + self.fibonacci(n - 1)


def fib():
    f = Fibonacci()
    for n in range(0, 32):
        print('Fibonacci #{0:d} = {1:d}'.format(n, f.fibonacci(n)))


if __name__ == '__main__':
    # main()
    t = timeit.Timer(stmt='fib', setup='')
    duration = t.repeat(1, 1)
    print(duration)
