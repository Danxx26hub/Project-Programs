#The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

print('What is the cost?')
cost = input()

print('How much money is given?')
given = input()

change = float(given) - float(cost)

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

while change > 0:
  
  if change % 100 == 0:
    change = change - 100
    hundred = hundred + 1

  elif change % 50 == 0:
    change = change - 50
    fifty = fifty + 1

  elif change % 20 == 0:
    change = change - 20
    twenty = twenty + 1

  elif change % 10 == 0:
    change = change - 10
    ten = ten + 1
