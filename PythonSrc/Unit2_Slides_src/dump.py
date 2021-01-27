#!/usr/bin/env python3

class BankAccount:
    def __init__(self, amount=0):
        self.balance = amount
    def print_balance(self):
        print(self.balance)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount


def dump(obj):
    assert(hasattr(obj, '__class__'))
    print('Dump of instance of {0:s}'.format(repr(obj.__class__)))
    for attr_name in dir(obj):
        if hasattr(obj, attr_name) and '__' not in attr_name:
            attr_val = str(getattr(obj, attr_name))
            attr_val = '<method>' if 'method' in attr_val else attr_val
            print('  obj.{0:s} = {1:s}'.format(attr_name, attr_val))


checking = BankAccount(100)
dump(checking)
