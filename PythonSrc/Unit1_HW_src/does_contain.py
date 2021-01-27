#!/usr/bin/env python3

def does_contain(items, x):
    for item in items:
        if item == x:
            return True
    return False


print(does_contain([1,2,3,4,5], 3))
print(does_contain([1,2,3,4,5], 7))
