#Calculate the total cost of tile it would take to cover a 
#floor plan of width and height, using a cost entered by the user.

print('What is the width?')
w = input()

print('What is the height?')
h = input()

print('What is the cost per unit of area?')
c = input()

tc = w * h * c

print('Total Cost: ' + str(tc))
