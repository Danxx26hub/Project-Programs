# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent

prompt = int(input("""1 for dec-->bin
2 for bin-->dec
> """))

choice = int(input('number> '))


if choice == 1:
    binary = bin(choice)
    print(binary)