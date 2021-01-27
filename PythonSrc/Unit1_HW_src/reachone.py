#!/usr/bin/env python3

def reachone_next(n: int) -> int:
    result = n / 2 if n % 2 == 0 else 3 * n + 1
    return result  # Comment this line to create an error


def reachone_step_count(n: int) -> int:
    count = 0
    while n > 1:
        count += 1
        n = reachone_next(n)
    return count


if __name__ == '__main__':
    n = 5777
    print('{0:d} --> {1:d}'.format(n, reachone_step_count(n)))
