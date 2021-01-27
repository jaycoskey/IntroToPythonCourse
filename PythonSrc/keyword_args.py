#!/usr/bin/env python3

def add_by_place(tens, ones):
    return 10 * tens + 1 * ones


print(add_by_place(5, 7))
print(add_by_place(tens=5, ones=7))
print(add_by_place(ones=5, tens=7))


s = '\n'.join(['Hello world!'] * 3)
print(s)
