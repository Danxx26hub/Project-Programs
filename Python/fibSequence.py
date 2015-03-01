# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.


def nthfib(number):
    fibterms = [0, 1]
    while len(fibterms) < int(number):
        fibterms.append(sum(fibterms[-2:]))
    return fibterms


def lessfib(num):
    fiblist = [0, 1]
    while sum(fiblist[-2:])< num:
        fiblist.append(sum(fiblist[-2:]))
    return fiblist


prompt = input('1 for first n fibs, 2 for fibs less than n> ')
prompt = int(prompt)

choice = input('What is N? ')
choice = int(choice)

if prompt == 1:
    print(nthfib(choice))

elif prompt == 2:
    print(lessfib(choice))

else:
    print('ERROR')