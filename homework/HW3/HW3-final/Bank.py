from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():

    # Should I be definining an initial balance here?
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

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
    
    # Struggling with returning the balance value.
    def __len__(self):
        return len(self.balance)


class BankUser():

    def __init__(self, owner):
        self.owner = owner
        self.checking = None
        self.savings = None
    
    # Not certain how to verify whether or not a user already has an account.
    # How to account for two specific accounts.
    def addAccount(self, accountType):
        # Possibly use enum syntax here AccountType.Checking.name

        if (accountType == AccountType.SAVINGS) and (self.savings == None):
            self.savings = AccountType.SAVINGS
            self.saving_balance = 0
            print("You have successfully created a {} account".format(self.savings.name))

        else:
            print("You have already opened a SAVINGS account.")

        if (accountType == AccountType.CHECKING) and (self.checking == None):
            self.checking = AccountType.CHECKING
            self.checking_balance = 0
            print("You have successfully created a {} account".format(self.checking.name))

        else: 
            print("You have already opened a CHECKINGS account.")

        # if accountType == "CHECKING":
        #     # self.checking = accountType
        #     self.checking_balance = 0
        #     print("You have successfully created a {} account".format(self.checking))
        # elif accountType == "SAVINGS":
        #     # self.savings = accountType
        #     self.saving_balance = 0
        #     print("You have successfully created a {} account".format(self.savings))
        # else:
        #     print("Please enter CHECKING or SAVINGS.")
            
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
            
        
        # if hasattr(self, accountType):
        #     print("You already have this type of account.")
        # else:
        #     self.accountType = accountType
        #     self.balance = 0
        #     print("You have successfully created a {} account".format(self.accountType))

    # How are we supposed to return a nonexistent balance? Where do we set the balance?
    def getBalance(self, accountType):
        
    def deposit(self, accountType, amount):
        self.balance += amount

    def withdraw(self, accountType, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Withrdawal over limit.")

    def __str__(self):
        return "Hello {0}, you have just created a {1} account!".format(self.owner, self.accountType)