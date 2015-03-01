# A happy number is defined by the following process.
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers,
# while those that do not end in 1 are unhappy numbers.
# Display an example of your output here. Find first 8 happy numbers.

def sumSqDigs(number):  # This works
    number = str(number)
    digs = []
    for dig in number:
        digs.append(dig)

    squares = []
    for item in digs:
        squares.append(int(item) ** 2)

    return sum(squares)

start = 26
current = start

while current != 1:
    print(current)
    current = sumSqDigs(current)

print(current)