#The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

print('What is the cost?')
cost = input()

print('How much money is given?')
given = input()

return = float(given) - float(cost)

hundred = 0
fifty = 0
twenty = 0
ten = 0
five = 0
one = 0
quarter = 0 
dime = 0
nickel = 0
penney = 0

while return > 0:
  
  if return % 100 = 0:
    return = return - 100
