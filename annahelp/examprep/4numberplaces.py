number = str(input('choose a number from 1000 - 9999: '))
if int(number) < 1000 or int(number) > 9999:
    exit()
number = list(number)

thousandths = number[0]
hundredths = number[1]
tenths = number[2]
ones = number[3]

print(thousandths, hundredths, tenths, ones)