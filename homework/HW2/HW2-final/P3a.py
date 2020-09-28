# Start Closure Definition
def make_withdrawal(init_balance):
  # Creating an empty list in which new withdrawal amounts can be added and accumulated.
  series = []

  def withdrawal_amount(new_value):

    # Codifying a condition to catch if the withdrawal amount is over the limit.
    if new_value > init_balance:
      print("Withdrawal over limit.")
      return None;

    # Adding values to the list to summate the withdrawals.
    series.append(new_value)
    new_bal = init_balance - sum(series)

    # Codifying a condition to catch if the withdrawal amount is over the limit.
    if new_bal <0:
      print("Withdrawal over limit.")
    else:
      return new_bal
  
  return withdrawal_amount

# End Closure Definition

# Demo

wd = make_withdrawal(1000)
wd(100)
wd(200)

## DEMO ERROR EXPLANATION ##

print('The withdrawal amounts are appended to the series list, which is bound to the closure. The items within the series are contained within cells and these cells are maintained in their own repository to be called upon when the function is later invoked. I found this interesting because I tested this function inside Jupyter notebook and found that the values were presented after each execution. This is not happening in terminal.')

## END DEMO EXPLANATION ##