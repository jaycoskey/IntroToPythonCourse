#!/usr/bin/env python3

cheeses = ['cheddar', 'feta', 'swiss']
cheeses[1] = 'brie'
temp = cheeses[2]
cheeses[2] = cheeses[0]
cheeses[0] = temp
print("I'll have the {0:s}, {1:s}, and {2:s}"
    .format(cheeses[0], cheeses[1], cheeses[2]))
