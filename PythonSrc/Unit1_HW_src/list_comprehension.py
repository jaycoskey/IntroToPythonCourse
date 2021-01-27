#!/usr/bin/env python3

a = [2**p for p in range(0, 5)]
b = [(p, 2**p) for p in range(0, 5)]
c = ['Hello'[k] for k in range(0, 5)]
d = ['KMGTE'[k] + '=10**' + str(3*k+3) for k in range(0, 5)]


print(a)
print(b)
print(c)
print(d)
