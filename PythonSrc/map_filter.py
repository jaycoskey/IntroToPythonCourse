#!/usr/bin/env python3

increment = lambda x: x + 1
is_even = lambda x: x % 2 == 0

items = range(0, 10)

lc = [increment(x) for x in items if is_even(x)]
mf = map(increment, filter(is_even, items))
fm = filter(is_even, map(increment, items))

mf = list(mf)
fm = list(fm)

print('lc={0:s}'.format(str(lc)))
print('mf={0:s}'.format(str(mf)))
print('fm={0:s}'.format(str(fm)))

