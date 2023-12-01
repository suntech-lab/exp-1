# practice 1
name = "Stefanos"

for element in name:
    print(element)

# practice 2

adj = ['large', 'small', 'bad', 'delicious']
food = ['pie', '羊肉炒面', 'watermelon', 'sushi']

for x in adj:
    for y in food:
        print(x, y)

# calculate the interest to track the growth of an investment

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f'year {year}: ${amount:,.2f}')


