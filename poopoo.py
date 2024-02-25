names = ""

accumulator_variable = 0

while True:

    name = str(input('Enter a Name: '))

    if name == '':
        print(f'Your names: {names}')
        break

    if accumulator_variable == 0:
        names += name
        accumulator_variable = 1

    elif accumulator_variable == 1:
        names += ', ' + name