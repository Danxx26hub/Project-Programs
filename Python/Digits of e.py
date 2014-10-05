#Enter a number and have the program generate e up to that many decimal places.

def eFormula(y):
    
    n = (1+(1/y))**y
    return n


print("How many decimal places?")
x = input()

a = 100000000000000000000000000000000000
while len(str(eFormula(a))) < int(x) - 2:
    a = a + 1

print(eFormula(a))

