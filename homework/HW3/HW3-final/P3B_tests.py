from Bank import BankAccount, BankUser

newUser = BankUser("Nishu")
newUser.addAccount("CHECKING")
newUser.deposit("CHECKING", 1000)
newUser.getBalance("CHECKING")
