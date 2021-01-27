#!/usr/bin/env python3

END = 3
print('Base -3 => Base 10:')
for a in range(0, END):
    for b in range(0, END):
        for c in range(0, END):
            n = 9 * a - 3 * b + c
            print('    {0:d}{1:d}{2:d} => {3:d}'.format(a, b, c, n))


print('   1000 => -27')
