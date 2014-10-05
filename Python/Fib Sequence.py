#Enter a number and have the program generate the Fibonacci
#sequence to that number or to the Nth number.

#Where there is a backslash, I need to tab over.

def nthFib(n):
  fibTerms = [0, 1]
  while len(fibTerms) < n-1:
    a = fibTerms(len(fibTerms)) - 1
    b = fibTerms(len(fibTerms)) - 2
    nextTerm = a + b
    fibTerms.append(nextTerm)
  return fibTerms

def lessFib(n):
  fibTerms = [0,1]
  while fibTerms[len(fibTerms) - 1] < n:
    a = fibTerms(len(fibTerms)) - 1
    b = fibTerms(len(fibTerms)) - 2
    nextTerm = a + b
    fibTerms.append(nextTerm)
  return fibTerms
  
print("For the first n Fibonacci terms, enter 1. For Fibonacci terms < n, enter 2.")
choice = input()
print("Now give your n value.")
n = input()

if choice = 1:
  print(nthFib(n))
  
  else:
    print(lessFib(n))
