#Asks the user to enter a cost and either a country or state tax. 
#It then returns the tax plus the total cost with tax.

print('What is the cost?')

cost = input()

print('What is the tax rate? (in %)')

rate = input()

tax = float(rate) * float(cost)

tc = tax + float(cost)

print('Tax cost: ' + tax)
print('Total cost: ' + tc)
