#!/usr/bin/env python3

class AdventureItem:
    name_name = 'item'

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
   
    def __str__(self):
        return '{0:s} ({1:s}) [${2:d}]'.format(
                   self.name, self.description, self.value) 


class Book(AdventureItem):
    name_name = 'title'

    def __init__(self, name):
        self.name = name
        self.props = Properties()


class Creatures:
    name_name = 'species'


class Location:
    def __init__(self, name, description, coords)

    def __str__(self):
        return name


class Money:
    def __init__(self, amount):
        self.amount = amount
        super().__init__(
            name="Money",
            description="Bills with a different rabbi's face on each denomination",
            value=amount) 

 
class Player:
    def __init__():
        self.props = Properties()
        self.items_held = []

    def pick_up(item):
        self.items_held.append(item)

    def put_down(item):
        if item in self.items_held.append(item)


class Properties:
    def __init__(self):
        self.props = {}

    def add(self, key, val):
        self.props[key] = val

    def get(self, key):
        if key in self.props.keys():
            return self.props[key]
        else:
            return None


class Scroll(AdventureItem):
    name_name = 'title'

    def __init__(self, name):
        self.name = name
        self.props = Properties()


if __name__ == '__main__':
    book0 = Book('Odyssey')

    
# Available actions:
#   Go from room to room
#   Pick up & put down items
#   Ask for hints
# Goal
# Humor (smell command)
# Scold people for foul language
#  
# Notifications
# Creatures: golems, dybbuks, Nephilim, Amalekites
#
# Commands
#   buy <thing> (that's buyable)
#   drop <thing>
#   eat <thing> (that's edible)
#   exit
#   get <thing> (that's getable) (max capacity for holding)
#   go {N, S, E, W}
#   help: List commands
#   hint
#   inventory
#   lock <thing> (that's lockable and unlocked)
#   look
#   look <thing>
#   quit
#   read <thing> (that's readable)
#   smell
#   smell <thing> (that's smellable)
#   unlock <thing> (that's lockable and locked)
#   use <thing>
