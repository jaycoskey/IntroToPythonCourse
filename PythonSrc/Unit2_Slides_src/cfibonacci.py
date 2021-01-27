#!/usr/bin/env python3

import timeit


class CFibonacci:
    computed_values = dict()

    def __init__(self):
        pass

    def fibonacci(self, n):
        assert(type(n) == int and n >= 0)
        if n in CFibonacci.computed_values.keys():
            return CFibonacci.computed_values[n]
        elif n == 0 or n == 1:
            return 1
        else:
            val = self.fibonacci(n - 2) + self.fibonacci(n - 1)
            CFibonacci.computed_values[n] = val
            return val


def main():
    f = CFibonacci()
    for n in range(0, 1001):
        print('Fibonacci #{0:d} = {1:d}'.format(n, f.fibonacci(n)))

 
if __name__ == '__main__':
    duration = timeit.repeat(stmt='main()',
                             setup='',
                             timer=timeit.default_timer,
                             repeat=1,
                             number=1)
    print(duration)
