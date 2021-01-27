#!/usr/bin/env python3

class Greeter:
    def __init__(self, greeting='Hello', name='world'):
        self.greeting = greeting
        self.name = name

    def greet(self):
        print(self.greeting + ', ' + self.name + '!')


if __name__ == '__main__':
    hw = Greeter('Hello', 'world')
    sp = Greeter('Hola', 'amigos')
    hw.greet()
    sp.greet()
