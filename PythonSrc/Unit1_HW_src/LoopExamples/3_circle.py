#!/usr/bin/env python3

for row in range(-6, 7):
    for col in range(-6, 7):
        if row ** 2 + col ** 2 <= 25:
            print('*', end='')
        else:
            print('.', end='')
    print()
