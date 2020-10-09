from enum import Enum

# Using enums to create an AccountType class with SAVINGS and CHECKINGS as constants.
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():

    # Defining initialization function with owner, accountType (from enum), and account balance.
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.accountType.balance = 0

    # Defining withdraw function, which decrements the balance amount from the specific account specified.
    def withdraw(self, amount):
        if self.accountType.balance >= amount:
            self.accountType.balance -= amount
            print("\n You have withdrawn ", amount)
        else:
            print("Withrdawal over limit.")

    def deposit(self, amount):
        self.accountType.balance += amount
        print("\n You have deposited ", amount)

    def __str__(self):
        return "Hello {0} you have accessed your {1} account!".format(self.owner, self.accountType)
    
    # Struggling with returning the balance value.
    def __len__(self):
        return len(self.accountType.balance)


class BankUser():

    def __init__(self, owner):
        self.owner = owner
        self.accountType = AccountType
        self.accountType.savings = None
        self.accountType.checking = None
    
    def addAccount(self, accountType):
        # Possibly use enum syntax here AccountType.Checking.name

        if (accountType == AccountType.SAVINGS.name) and (self.accountType.savings == None):
            self.accountType.savings = AccountType.SAVINGS
            self.accountType.savings.balance = 0
            print("You have successfully created a {} account".format(self.accountType.savings.name))

        elif (accountType == AccountType.CHECKING.name) and (self.accountType.checking == None):
            self.accountType.checking = AccountType.CHECKING
            self.accountType.checking.balance = 0
            print("You have successfully created a {} account".format(self.accountType.checking.name))

        elif (accountType == AccountType.SAVINGS.name) and (self.accountType.savings != None):
            print("You have already opened a SAVINGS account.")
        elif (accountType == AccountType.CHECKING.name) and (self.accountType.checking != None):
            print("You have already opened a CHECKINGS account.")
            
    def deposit(self, accountType, amount):
        if accountType == "CHECKING":
            self.checking_balance += amount
        elif accountType == "SAVINGS":
            self.saving_balance +=amount

    def withdraw(self, accountType, amount):
        if accountType == "CHECKING":
            if self.checking_balance >= amount:
                self.checking_balance += amount
        elif accountType == "SAVINGS":
            if self.checking_balance >= amount:
                self.checking_balance += amount
        else:
            print("Withdrawal over limit.")
            
    # How are we supposed to return a nonexistent balance? Where do we set the balance?
    def getBalance(self, accountType):
        
    def deposit(self, accountType, amount):
        self.accountType.balance += amount

    def withdraw(self, accountType, amount):
        if self.accountType.balance >= amount:
            self.accountType.balance -= amount
        else:
            print("Withrdawal over limit.")

    def __str__(self):
        return "Hello {0}, you have just created a {1} account!".format(self.owner, self.accountType)