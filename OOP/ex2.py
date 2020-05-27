"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit accepted.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds unavailable!")
        else:
            self.balance -= amount
            print("Withdraw accepted.")

    def __str__(self):
        return f"\nAccount owner:   {self.owner}\nAccount balance: {self.balance} $\n"


acct1 = Account('Martin', 100)
acct1.deposit(400)
print(acct1)
acct1.withdraw(350)
print(acct1)
acct1.withdraw(400)
