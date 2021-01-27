#!/usr/bin/env python3

for row in range(1, 7):
    for col in range(1, 7):
        total = row + col
        if total == 7:
            print('    *', end='')
        else:
            print('{0:5d}'.format(row+col), end='')
    print()
