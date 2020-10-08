from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():

    def __init__(self, owner, accountType: AccountType, balance):
        self.owner = owner
        self.accountType = accountType
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\n You have withdrawn ", amount)
        else:
            print("Withrdawal over limit.")


    def deposit(self, amount):
        self.balance += amount
        print("\n You have deposited ", amount)

    def __str__(self):
        return "Hello {0} you have accessed your {1} account!".format(self.owner, self.accountType)
    
    def __len__(self):
        return len(self.balance)

a1 = BankAccount("Nishu", "CHECKING", 100000)

a1.deposit(1000)
a1.withdraw(5000)
str(a1)
len(a1)