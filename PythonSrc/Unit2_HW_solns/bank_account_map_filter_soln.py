#!/usr/bin/env python3

class NamedBankAccount:
    """A bank account that stores the name of the account owner.
    The class also maintains a class-level dictionary of all accounts
    by account-holder name."""

    # A dict, with account names as keys, and accounts as values.
    accounts = {}

    def print_balances():
        for name in NamedBankAccount.accounts.keys():
            # Look up the account in the class-level registry.
            NamedBankAccount.accounts[name].print_balance()

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        # Register new account in the class-level list of accounts.
        NamedBankAccount.accounts[name] = self

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def print_balance(self):
        print('Balance({0:s})=${1:.2f}'.format(self.name, self.balance))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        assert(amount <= self.balance)
        self.balance -= amount


if __name__ == '__main__':
    accts_data = [ ('Amy', 300.00), ('Brad', 400.00), ('Cindy', 500.00) ]

    # DONE: Use map to get [ NamedBankAccount(name, amount) for (name, amount) in acct_data ]
    accts = map(lambda pair: NamedBankAccount(pair[0], pair[1]), accts_data)

    # TODO: Use filter to get a list of only those accounts that have at least $400.
    # SO accts_min_400 = [ acct for acct in accts if acct.get_balance() >= 400 ]
    accts_min_400 = filter(lambda acct: acct.get_balance() >= 400, accts)

    for acct in accts_min_400:
        acct.print_balance() 
