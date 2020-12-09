divisible = False
while not divisible:
    first = int(input('Enter a number: '))
    second = int(input('Enter a second (divisible by the first): '))

    divisible = first % second == 0

print(f'{first} and {second} are divisibile!')
