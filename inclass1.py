# tax and tip calculator

BC_TAX = 0.07
TIP = 0.12

price = float(input('enter the price of your meal and this will calculate the tax and tip: '))

tax = (price * BC_TAX)
tip = (price * TIP)
total = (price * BC_TAX + price * TIP + price)

print(f'your tip for this meal is ${tip:.2f}, your tax for this meal is ${tax:.2f}, and your total is ${total:.2f}.')

# sum of first n positive integers

num = int(input('which number do you want: '))

def triangle(num):
    num = (num * (num + 1))/2
    return num

print(triangle(num))

# write a code that tells the user whether the input is even or odd

integer = int(input('input an integer here: '))

if integer % 2 == 0:
    print('this is an even integer')
else:
    print('this is an odd integer')