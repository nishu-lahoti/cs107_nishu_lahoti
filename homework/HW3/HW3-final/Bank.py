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
            print("\nYou have withdrawn {0} amount from your {1} account. Your total balance is now {2}.".
            format(amount, self.accountType.name, self.balance))

        elif self.balance < amount:
            print("\nWithdrawal over limit. You only have {0} amount in your {1} account. Your total balance is now {2}.".
            format(self.accountType.balance, self.accountType.name, self.balance))

    def deposit(self, amount):

        if amount < 0:
            print("\n You cannot deposit a negative amount.")
        elif amount >= 0:
            self.balance += amount
            print("\nYou have deposited {0} into your {1} account. Your total balance is now {2}.".
            format(amount, self.accountType.name, self.balance))

    def __str__(self):
        return "\nHello {0} you have accessed your {1} account!".format(self.owner, self.accountType.name)
    
    # Struggling with returning the balance value.
    def __len__(self):
        return self.balance


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
            x = len(self.savings)
            return ("You have {} in your SAVINGS account.").format(x)

        elif (accountType == AccountType.CHECKING):
            x = len(self.checking)
            return ("You have {} in your CHECKING account.").format(x)

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


def ATMSession(bankUser: BankUser):
    
    def Interface():
        
        while True:

            try:
                userInput = int(input("Enter Option: \n1) Exit \n2) Create Account \n3) Check Balance \n4) Deposit \n5) Withdraw \n"))

            except ValueError:
                print("Error! This is not a number. Try again.")

            if userInput == 1:
                print("Thank you and goodbye!")
                break
                
            elif userInput == 2:
                try:
                    inputAccount = int(input("Enter Option: \n1) Checking \n2) Savings\n"))

                    if inputAccount == 1:
                            bankUser.addAccount(AccountType.CHECKING)
                            checking_amount = int(input("Enter Integer Amount, Cannot Be Negative: "))
                            bankUser.deposit(AccountType.CHECKING, checking_amount)
                        
                    elif inputAccount == 2:
                            bankUser.addAccount(AccountType.SAVINGS)
                            saving_amount = int(input("Enter Integer Amount, Cannot Be Negative: "))
                            bankUser.deposit(AccountType.SAVINGS, saving_amount)

                except ValueError:
                    print("Error! You must enter either 1 or 2. Try again.")
            
            elif userInput == 3:
                try:
                    inputAccount = int(input("Enter Option: \n1) Checking \n2) Savings\n"))

                    if inputAccount == 1:
                            bankUser.getBalance(AccountType.CHECKING)
                        
                    elif inputAccount == 2:
                            bankUser.getBalance(AccountType.SAVINGS)

                except ValueError:
                    print("Error! You must enter either 1 or 2. Try again.")

            elif userInput == 4:
                try:
                    inputAccount = int(input("Enter Option: \n1) Checking \n2) Savings\n"))

                    if inputAccount == 1:
                            deposit_amt = int(input("Enter Integer Amount, Cannot Be Negative: "))
                            bankUser.deposit(AccountType.CHECKING, deposit_amt)
                        
                    elif inputAccount == 2:
                            deposit_amt = int(input("Enter Integer Amount, Cannot Be Negative: "))
                            bankUser.deposit(AccountType.SAVINGS, deposit_amt)

                except ValueError:
                    print("Error! You must enter either 1 or 2. Try again.")

            elif userInput == 5:
                try:
                    inputAccount = int(input("Enter Option: \n1) Checking \n2) Savings\n"))

                    if inputAccount == 1:
                            withdraw_amt = int(input("Enter Integer Amount, Cannot Be Negative: "))
                            bankUser.withdraw(AccountType.CHECKING, withdraw_amt)
                        
                    elif inputAccount == 2:
                            withdraw_amt = int(input("Enter Integer Amount, Cannot Be Negative: "))
                            bankUser.withdraw(AccountType.SAVINGS, withdraw_amt)

                except ValueError:
                    print("Error! You must enter either 1 or 2. Try again.")

    return Interface()


newUser = BankUser("Nishu")
ATMSession(newUser)