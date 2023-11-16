# ask the user to input a number and then round it to two decimal places
n = float(input('enter your decimal number: '))
print(round(n, 2))

# ask the user to input a number and then show its absolute value
n2 = int(input('enter your integer: '))
print('the absolute value of ', n2, 'is ', abs(n2))

# ask the user for 2 numbers and display whether the difference is two integers
n3 = str(input('enter your first number: '))
n4 = str(input('enter your second number: '))
if (float(n3) - float(n4)) % 1 == 0:
    print('the difference IS an integer')
else:
    print('the difference is NOT an integer')

# print the result of 3 ** .125 as  fixed-point number with three decimal places
result = 3 ** 0.125
print(f'{result} written as a fixed point number with three decimal places is {result:.3f}')

# print the number 150000 as a currency with two decimal places, with the thousands grouped with commas
dollars = 150000
print(f'i have ${dollars:,.2f} dollars')

# print the result of 2 / 10 as a percentage with no decimal places
n5 = 2 / 10
print(f'2 / 10 printed as a percentage with no decimal places is {n5:.0%}')
