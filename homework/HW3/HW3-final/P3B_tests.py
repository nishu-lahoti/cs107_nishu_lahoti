from Bank import AccountType, BankAccount, BankUser

def test_over_withdrawal(): #this test function should throw an Exception or Error 
    newUser = BankUser("Nishu")
    newUser.addAccount(AccountType.CHECKING)
    newUser.deposit(AccountType.CHECKING, 500)

    try:
        newUser.withdraw(AccountType.CHECKING, 1000)
    except Exception as excep:
        print(excep)


def test_null_account(): #this tests whether or not the account exists
    newUser = BankUser("Nishu")
    newUser.addAccount(AccountType.SAVINGS)
    newUser.deposit(AccountType.SAVINGS, 1000)

    try:
        newUser.deposit(AccountType.CHECKING, 1000)
    except Exception as excep:
        print(excep)

def withdraw_negative_amount(): #this tests if the user is trying to withdraw a negative amount
    newUser = BankUser("Nishu")
    newUser.addAccount(AccountType.SAVINGS)
    newUser.deposit(AccountType.SAVINGS, 1000)

    try:
        newUser.withdraw(AccountType.SAVINGS, -100)
    except Exception as excep:
        print(excep)

def test_duplicate_account(): #this tests if the accounta already exists
    newUser = BankUser("Nishu")
    newUser.addAccount(AccountType.CHECKING)

    try:
        newUser.addAccount(AccountType.CHECKING)
    except Exception as excep:
        print(excep)

def test_get_balance(): #this tests if the user is trying to get a balance for a nonexistent account
    newUser = BankUser("Nishu")
    newUser.addAccount(AccountType.CHECKING)
    newUser.deposit(AccountType.CHECKING, 1000)

    try:
        newUser.getBalance(AccountType.SAVINGS)
    except Exception as excep:
        print(excep)

  
test_over_withdrawal()
test_null_account()
withdraw_negative_amount()
test_duplicate_account()
test_get_balance()