#Write some code that simulates flipping a single coin however many times the user decides. 
#The code should record the outcomes and count the number of tails and heads.

import random

print('How many flips?')
flips = input()

count = 0

tails = 0
heads = 0

n = 0

while int(count) < int(flips):
  n = random.randint(1,2)
  
  if n == 1:
    tails = tails + 1
  
  else:
    heads = heads + 1

print('Tails: ' + str(tails))
print('Heads: ' + str(heads))
