def shipping_charge(number_of_items):
    cost = (number_of_items - 1) * 2.95 + 10.95
    return cost

number_of_items = int(input('how many items to calculate?: '))
if number_of_items < 0:
    print('dont even think about making any money bud')
else:
    print(f'you have purchased {number_of_items} items. the cost to ship {number_of_items} items is ${shipping_charge(number_of_items):,.2f} dollars')
