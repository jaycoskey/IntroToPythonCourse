#!/usr/bin/env python3

from functools import reduce

print(reduce(lambda x,y: x+y, [1,2,3,4,5]))
