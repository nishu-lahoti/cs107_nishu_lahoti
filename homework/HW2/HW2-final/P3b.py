## START CLOSURE DEFINITION ##

def make_withdrawal(init_balance):
  series = []

# Creating an empty list in which new withdrawal amounts can be added and accumulated.

  def withdrawal_amount(new_value):
    # Codifying a condition to catch if the withdrawal amount is over the limit.
    if new_value > init_balance:
      print("Withdrawal over limit.")
      return None;

    # Updated the function to decrement init_balance directly.
    series.append(new_value)
    new_bal = sum(series)
    init_balance -= new_bal

    # Codifying a condition to catch if the withdrawal amount is over the limit.
    if init_balance <0:
      print("Withdrawal over limit.")
    else:
      return init_balance
  
  return withdrawal_amount

## END CLOSURE DEFINITION ##

## DEMO ERROR EXPLANATION ##

print('''\nWhen running this code, the terminal noted that "init_balance was referenced before assignment." This is due to a variable binding issue. init_balance is defined a local variable, not a global or nonlocal variable, and thus when we try to assign it within a closure, Python does not recognize it as a defined variable.\n''')

## END DEMO ERROR EXPLANATION ##

## Demo
wd = make_withdrawal(1000)
wd(100)
wd(200)