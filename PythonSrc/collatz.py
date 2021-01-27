#!/usr/bin/env python3

import matplotlib.pyplot as plt


def collatz_next(n: int) -> int:
    result = n / 2 if n % 2 == 0 else 3 * n + 1
    return result  # Comment this line to create an error


def collatz_step_count(n: int) -> int:
    count = 0
    while n > 1:
        count += 1
        n = collatz_next(n)
    return count


xs = range(1,10001)
ys = [collatz_step_count(x) for x in xs]


plt.scatter(xs, ys)
plt.show()
