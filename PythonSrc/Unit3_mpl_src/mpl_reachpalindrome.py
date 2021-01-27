#!/usr/bin/env python3
# Recall the "reachone" system in HW #4, question 2(b).
#   There was a step function f(n), with a single int argument, and returns an int.
#   There was a "stopping condition"---namely, when the number reached one.
# In this script,
#   the step function is to add the number n to its "reverse", int(str(n)[::-1]).
#   the stopping condition is when the number becomes a palindrome.

import matplotlib.pyplot as plt


def is_palindrome(n):
    return str(n) == str(n)[::-1]

    
def reachpalindrome_next(n: int) -> int:
    return n + int(str(n)[::-1])


def reachpalindrome_step_count(n: int) -> int:
    count = 0
    while (not is_palindrome(n)):
        count += 1
        n = reachpalindrome_next(n)
    return count


pxs = range(1,101)
pys = [reachpalindrome_step_count(px) for px in pxs]


plt.scatter(pxs, pys)
plt.title('ReachPalindrome steps')
plt.xlim(-1,101)
plt.ylim(-1,25)
plt.xlabel('Value')
plt.ylabel('Step count')
for px in pxs:
    if pys[px - 1] > 10:
        py = pys[px - 1]
        plt.annotate('({0},{1})'.format(px,py), xy=(px,py), xytext=(px-50,py-5-(px-89)), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
