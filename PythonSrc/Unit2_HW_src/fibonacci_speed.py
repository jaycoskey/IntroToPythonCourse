#!/usr/bin/env python3

import time


class Fibonacci:
    def __init__(self):
        pass

    def fibonacci(self, n):
        assert(type(n) == int and n >= 0)
        if n == 0 or n == 1:
            return 1
        else:
            return self.fibonacci(n - 2) + self.fibonacci(n - 1)


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


def get_fib_32_execution_time():
    f = Fibonacci()
    begin_time = time.clock()
    for n in range(0, 32):
        print('Fibonacci #{0:d} = {1:d}'.format(n, f.fibonacci(n)))
    end_time = time.clock()
    return end_time - begin_time


def get_cfib_5000_execution_time():
    cf = CFibonacci()
    begin_time = time.clock()
    for n in range(0, 5000):
        print('Cached Fibonacci #{0:d} = {1:d}'.format(n, cf.fibonacci(n)))
    end_time = time.clock()
    return end_time - begin_time

 
if __name__ == '__main__':
    f32_time = get_fib_32_execution_time()
    cf5000_time = get_cfib_5000_execution_time()
    print()
    print('Computations complete!')
    print('Time to compute 32 Fibonacci values (uncached): {0:.4f} seconds'.format(f32_time))
    print('Time to compute 5000 Fibonacci values (cached): {0:.4f} seconds'.format(cf5000_time))
