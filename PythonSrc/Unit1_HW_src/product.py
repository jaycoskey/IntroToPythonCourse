#!/usr/bin/env python3

def product(items):
    product = 1
    for v in items:
        product *= v
    return product


print(product([1,2,3,4,5]))
