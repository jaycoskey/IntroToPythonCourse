#!/usr/bin/env python3

s = 'banana'
for i in range(0, len(s)):
    for j in range(i, len(s)):
        print(s[j], end='')
    print()
