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

        if self.balance >= amount:
            self.balance -= amount
            print("\nYou have withdrawn {0} amount from your {1} account.".format(amount, self.accountType))

        elif self.balance < amount:
            print("\nWithdrawal over limit. You only have {0} amount in your {1} account.".format(self.accountType.balance, self.accountType))

    def deposit(self, amount):

        self.balance += amount
        print("\nYou have deposited {0} into your {1} account.".format(amount, self.accountType))

    def __str__(self):
        return "\nHello {0} you have accessed your {1} account!".format(self.owner, self.accountType)
    
    # Struggling with returning the balance value.
    def __len__(self):
        return len(self.accountType.balance)


class BankUser():

    def __init__(self, owner):
        self.owner = owner
        # self.accountType = BankAccount(owner)
        self.savings = None
        self.checking = None
    
    def addAccount(self, accountType):
        # Possibly use enum syntax here AccountType.Checking.name
        # Define savings as a Bank Account object

        if (accountType == AccountType.SAVINGS.name) and (self.savings == None):
            # Using BankAccount object
            self.savings = BankAccount(self.owner, accountType)
            self.balance = 0
            print("{}".format(self.savings))
            return self.savings

        elif (accountType == AccountType.CHECKING.name) and (self.checking == None):
            self.checking = BankAccount(self.owner, accountType)
            self.balance = 0
            print("{}".format(self.checking))
            return self.checking

        elif (accountType == AccountType.SAVINGS.name) and (self.savings != None):
            print("\nYou have already opened a SAVINGS account.")

        elif (accountType == AccountType.CHECKING.name) and (self.checking != None):
            print("\nYou have already opened a CHECKING account.")
        
        else:
            print("\nPlease enter the correct type of account, SAVINGS or CHECKING.")
    
    def getBalance(self, accountType):

        if (accountType == AccountType.SAVINGS.name):
            # print("You have {} in your SAVINGS account.").format(self.accountType.savings.balance)
            return self.savings.balance

        elif (accountType == AccountType.CHECKING.name):
            # print("You have {} in your CHECKING account.").format(self.accountType.checking.balance)
            return self.checking.balance

        else:
            print("You do not have this type of account. Please enter CHECKING or SAVINGS.")

    def deposit(self, accountType, amount):

        if (accountType == AccountType.SAVINGS.name) and (self.savings != None):
            self.savings.deposit(amount)
            return self.savings

        elif (accountType == AccountType.CHECKING.name) and (self.checking != None):
            self.checking.deposit(amount)
            return self.checking

        else:
            print("\nYou do not have this type of account. Please open CHECKING or SAVINGS.")

    def withdraw(self, accountType, amount):

        if (accountType == AccountType.SAVINGS.name) and (self.savings != None):
            self.savings.withdraw(amount)
            
        elif (accountType == AccountType.CHECKING.name) and (self.checking != None):
            self.checking.withdraw(amount)
        
        else:
            print("\nYou do not have this type of account. Please open CHECKING or SAVINGS.")

    def __str__(self):
        return "Hello {0}, you have just created a {1} account!".format(self.owner, self.accountType)








# class BankAccount():

#     # Defining initialization function with owner, accountType (from enum), and account balance.
#     def __init__(self, owner, accountType: AccountType):
#         self.owner = owner
#         self.accountType = accountType
#         # self.accountType.balance = 0

#     # Defining withdraw function, which decrements the balance amount from the specific account specified.
#     def withdraw(self, amount):   

#         if self.accountType.balance >= amount:
#             self.accountType.balance -= amount
#             print("\n You have withdrawn ", amount)
#         else:
#             print("Withdrawal over limit.")

#     def deposit(self, amount):
#         self.accountType.balance += amount
#         print("\n You have deposited ", amount)

#     def __str__(self):
#         return "Hello {0} you have accessed your {1} account!".format(self.owner, self.accountType)
    
#     # Struggling with returning the balance value.
#     def __len__(self):
#         return len(self.accountType.balance)


# class BankUser():

#     def __init__(self, owner):
#         self.owner = owner
#         # self.accountType = BankAccount(owner)
#         self.savings = None
#         self.checking = None
    
#     def addAccount(self, accountType):
#         # Possibly use enum syntax here AccountType.Checking.name
#         # Define savings as a Bank Account object

#         if (accountType == AccountType.SAVINGS.name) and (self.accountType.savings == None):
#             # Using BankAccount object
#             self.savings = BankAccount(self.owner, accountType)
#             self.accountType.savings.balance = 0
#             print("You have successfully created a {} account".format(self.accountType.savings.name))
#             return self.accountType.savings

#         elif (accountType == AccountType.CHECKING.name) and (self.accountType.checking == None):
#             self.accountType.checking = AccountType.CHECKING
#             self.accountType.checking.balance = 0
#             print("You have successfully created a {} account".format(self.accountType.checking.name))
#             return self.accountType.checking

#         elif (accountType == AccountType.SAVINGS.name) and (self.accountType.savings != None):
#             print("You have already opened a SAVINGS account.")

#         elif (accountType == AccountType.CHECKING.name) and (self.accountType.checking != None):
#             print("You have already opened a CHECKINGS account.")
    
#     def getBalance(self, accountType):

#         if (accountType == AccountType.SAVINGS.name):
#             # print("You have {} in your SAVINGS account.").format(self.accountType.savings.balance)
#             return self.accountType.savings.balance

#         elif (accountType == AccountType.CHECKING.name):
#             # print("You have {} in your CHECKING account.").format(self.accountType.checking.balance)
#             return self.accountType.checking.balance

#         else:
#             print("You do not have this type of account. Please enter CHECKING or SAVINGS.")

#     def deposit(self, accountType, amount):
#         if (accountType == AccountType.SAVINGS.name):
#             self.accountType.savings.balance += amount
#             return self.accountType.savings

#         elif (accountType == AccountType.CHECKING.name):
#             self.accountType.checking.balance += amount
#             return self.accountType.checking
#         else:
#             print("You do not have this type of account. Please enter CHECKING or SAVINGS.")

#     def withdraw(self, accountType, amount):

#         if (accountType == AccountType.SAVINGS.name) and (self.accountType.savings.balance >= amount):
#             self.accountType.savings.balance -= amount
#             print("You have successfully withdrawn {0} from your SAVING account. You have {1}".format(amount, self.accountType.savings.balance))
#             return self.accountType.savings

        
#         elif (accountType == AccountType.CHECKING.name) and (self.accountType.checking.balance >= amount):
#             self.accountType.checking.balance -= amount
#             print("You have successfully withdrawn {0} from your CHECKING account. You have {1}".format(amount, self.accountType.checking.balance))
#             return self.accountType.savings

#         elif (accountType == AccountType.SAVINGS.name) and (self.accountType.savings.balance < amount):
#             print("Withdrawal over limit. You only have {} amount in your SAVINGS account.".format(self.accountType.savings.balance))

#         elif (accountType == AccountType.CHECKING.name) and (self.accountType.checking.balance < amount):
#             print("Withdrawal over limit. You only have {} amount in your CHECKING account.".format(self.accountType.checking.balance))
        
#         else:
#             print("You do not have this type of account. Please enter CHECKING or SAVINGS.")

#     def __str__(self):
#         return "Hello {0}, you have just created a {1} account!".format(self.owner, self.accountType)