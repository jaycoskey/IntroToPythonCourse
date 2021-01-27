#!/usr/bin/env python3

class Human:
    tallest = None  # Equalling None is like not having a value.
    def get_tallest():
        return Human.tallest

    def __init__(self, name, height):
        self.name = name
        self.height = height
        if Human.tallest == None or height > Human.tallest.height:
            Human.tallest = self

    def greet(self):
        print('Hi, {0:s}'.format(self.name))


if __name__ == '__main__':
    amy = Human('Amy', 5.5)
    amy = Human('Bob', 6.0)
    amy = Human('Cindy', 7.5)
    print('Tallest: {0:s}'.format(Human.get_tallest().name))
