#Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

print("What is n?")
n = input()
steps = 0
while n != 1:
  
  if int(n) % 2 == 0:
    n = int(n)/2
    steps = steps + 1
    
  else:
    n = 3*int(n) + 1
    steps = steps + 1
    
print('Steps:' + str(steps))
