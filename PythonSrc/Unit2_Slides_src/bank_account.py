#!/usr/bin/env python3

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def print_balance(self):
        print('Balance=${0:.2f}'.format(self.balance))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        assert(amount <= self.balance)
        self.balance -= amount


if __name__ == '__main__':
    checking = BankAccount(100)
    checking.print_balance()
    savings = BankAccount()
    savings.deposit(250)
    savings.print_balance()
