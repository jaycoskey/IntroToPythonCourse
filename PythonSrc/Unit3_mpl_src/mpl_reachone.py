#!/usr/bin/env python3
# See Question 2(b) on HW #4.

import matplotlib.pyplot as plt


def reachone_next(n: int) -> int:
    result = n / 2 if n % 2 == 0 else 3 * n + 1
    return result


def reachone_count(n: int) -> int:
    count = 0
    while n > 1:
        count += 1
        n = reachone_next(n)
    return count


xs = range(1,10001)
ys = [reachone_count(x) for x in xs]


plt.scatter(xs, ys)
plt.show()
