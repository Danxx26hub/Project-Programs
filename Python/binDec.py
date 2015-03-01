# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent

prompt = int(input("""1 for dec-->bin
2 for bin-->dec
> """))

choice = input('number> ')

if prompt == 1:
    choice = int(choice)
    binary = bin(choice)
    binary = str(binary)
    print(binary[2:])

if prompt == 2:
    decimal = int(x=choice, base=2)
    print(decimal)