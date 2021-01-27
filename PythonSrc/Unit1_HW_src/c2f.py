#!/usr/bin/env python3

def c2f(celcius):
    return (9/5)*celcius + 32


assert(c2f(-40) == -40)
assert(c2f(0)   == 32)
assert(c2f(100) == 212)
