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
        self.balance = 0

    # Defining withdraw function, which decrements the balance amount from the specific account specified.
    def withdraw(self, amount):   

        if amount < 0:
            print("\nYou cannot withdraw a negative amount.")

        elif self.balance >= amount:
            self.balance -= amount
            print("\nYou have withdrawn {0} amount from your {1} account.".format(amount, self.accountType))

        elif self.balance < amount:
            print("\nWithdrawal over limit. You only have {0} amount in your {1} account.".format(self.accountType.balance, self.accountType))

    def deposit(self, amount):

        if amount < 0:
            print("\n You cannot deposit a negative amount.")
        elif amount >= 0:
            self.balance += amount
            print("\nYou have deposited {0} into your {1} account.".format(amount, self.accountType))

    def __str__(self):
        return "\nHello {0} you have accessed your {1} account!".format(self.owner, self.accountType)
    
    # Struggling with returning the balance value.
    def __len__(self):
        return len(self.balance)


class BankUser():

    def __init__(self, owner):
        self.owner = owner
        # self.accountType = BankAccount(owner)
        self.savings = None
        self.checking = None
    
    def addAccount(self, accountType):
        # Possibly use enum syntax here AccountType.Checking.name
        # Define savings as a Bank Account object

        if (accountType == AccountType.SAVINGS) and (self.savings == None):
            # Using BankAccount object
            self.savings = BankAccount(self.owner, accountType)
            self.balance = 0
            print("{}".format(self.savings))
            return self.savings

        elif (accountType == AccountType.CHECKING) and (self.checking == None):
            self.checking = BankAccount(self.owner, accountType)
            self.balance = 0
            print("{}".format(self.checking))
            return self.checking

        elif (accountType == AccountType.SAVINGS) and (self.savings != None):
            print("\nYou have already opened a SAVINGS account.")

        elif (accountType == AccountType.CHECKING) and (self.checking != None):
            print("\nYou have already opened a CHECKING account.")
        
        elif (accountType != (AccountType.CHECKING or AccountType.SAVINGS)):
            print("\nPlease enter the correct type of account, SAVINGS or CHECKING.")
    
    def getBalance(self, accountType):

        if (accountType == AccountType.SAVINGS):
            # print("You have {} in your SAVINGS account.").format(self.accountType.savings.balance)
            return len(self.savings)

        elif (accountType == AccountType.CHECKING):
            # print("You have {} in your CHECKING account.").format(self.accountType.checking.balance)
            return len(self.checking)

        else:
            print("You do not have this type of account. Please enter CHECKING or SAVINGS.")

    def deposit(self, accountType, amount):

        if (accountType == AccountType.SAVINGS) and (self.savings != None):
            self.savings.deposit(amount)
            return self.savings

        elif (accountType == AccountType.CHECKING) and (self.checking != None):
            self.checking.deposit(amount)
            return self.checking

        else:
            print("\nYou do not have this type of account. Please open CHECKING or SAVINGS.")

    def withdraw(self, accountType, amount):

        if (accountType == AccountType.SAVINGS) and (self.savings != None):
            self.savings.withdraw(amount)
            
        elif (accountType == AccountType.CHECKING) and (self.checking != None):
            self.checking.withdraw(amount)
        
        else:
            print("\nYou do not have this type of account. Please open CHECKING or SAVINGS.")

    def __str__(self):
        return "Hello {0}, you have just created a {1} account!".format(self.owner, self.accountType)


def ATMSession(bankUser):

    newUser = BankUser(bankUser)
    
    def Interface(userInput):
        
        try:
            userInput = int(input("Enter Option: \n1) Exit \n2) Create Account \n3) Check Balance \n4) Deposit \n5) Withdraw \n"))

        except ValueError:
            print("Error! This is not a number. Try again.")

        
        if userInput == 1:
            print("Thank you and goodbye!")
            
        elif userInput == 2:
            try:
                inputAccount = int(input("Enter Option: \n1) Checking \n 2) Savings"))

                if inputAccount == 1:
                        newUser.addAccount(AccountType.CHECKING)
                        checking_amount = int(input("Enter Integer Amount, Cannot Be Negative: "))
                        newUser.deposit(AccountType.CHECKING, checking_amount)
                    
                elif inputAccount == 2:
                        newUser.addAccount(AccountType.SAVINGS)
                        saving_amount = int(input("Enter Integer Amount, Cannot Be Negative: "))
                        newUser.deposit(AccountType.SAVINGS, saving_amount)

            except ValueError:
                print("Error! You must enter either 1 or 2. Try again.")

    return Interface


ATMSession("Nishu")