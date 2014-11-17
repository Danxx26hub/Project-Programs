#Write some code that simulates flipping a single coin however many times the user decides. 
#The code should record the outcomes and count the number of tails and heads.

import random

print('How many flips?')
flips = input()

count = 0

tails = 0
heads = 0

while int(count) < int(flips):
