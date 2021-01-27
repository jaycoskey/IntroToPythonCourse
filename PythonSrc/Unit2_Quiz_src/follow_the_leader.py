#!/usr/bin/env python3

import sys


class Player:
    latest = None 

    def greet_latest():
        if Player.latest == None:
            print('ERROR: No player created yet')
            assert(False)
        else:
            print('Howdy, {0:s}!'.format(Player.latest.name))

    def __init__(self, name):
        self.name = name
        Player.latest = self

    def greet(self):
        print('Hi, {0:s}!'.format(self.name))


a = Player('Amy')
Player.greet_latest()
b = Player('Bob')
Player.greet_latest()
c = Player('Cindy')


a.greet()
Player.greet_latest()
b.greet()
Player.greet_latest()
