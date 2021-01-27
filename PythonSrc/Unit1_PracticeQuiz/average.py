#!/usr/bin/env python3

def average(items):
    count = 0
    total = 0
    for k in items:
        count += 1
        total += k
    return total / count


items = [1,2,3,4,5, 6]        
print('Average of {0:s} is {1:.4f}.'.format(str(items), average(items)))
