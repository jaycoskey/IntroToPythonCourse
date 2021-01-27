#!/usr/bin/env python3

s = 'antes'
for i in range(0, len(s)):
    for j in range(0, i):
        print(s[j], end='')
    print()
