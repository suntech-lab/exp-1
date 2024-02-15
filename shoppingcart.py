class Dairy(object):
    def __init__(self):
        pass

    def desc(self):
        print('this product is dairy')

class Frozen(object):
    def __init__(self):
        pass

    def desc(self):
        print('this product is frozen')

class Vegetable(object):
    def __init__(self):
        pass

    def desc(self):
        print('this product is a vegetable')

class ShoppingCart(object):

    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(f'{product} added.')
            
        else:
            print(f'{product} is already in cart.')

    def remove_item(self, product):
        if product in self.items_in_cart:
            self.items_in_cart.pop(product)
            print(f'{product} removed.')

        else:
            print(f'{product} is not in cart.')

    def total_price(self):
        print(f"The total value of the items in {self.customer_name}'s cart is ${sum(self.items_in_cart.values()):,.2f}")
        if sum(self.items_in_cart.values()) > 50:
            print('You are eligible for free shipping!')

shop_items = [
    {'item': 'Laptop',            'price':      200},
    {'item': 'Thermos',           'price':       35},
    {'item': 'Roast Chicken',     'price':     12.5},
    {'item': 'Sack of Potatoes',  'price':      5.5},
    {'item': 'Dr. Martens Boots', 'price':      212},
    {'item': 'Jellyfish Lamp',    'price':      8.1},
    {'item': 'Romance Novel',     'price':    10.25},
    {'item': '15 Pound Dumbells', 'price':     9.50},
    {'item': 'Headphones',        'price':     70.8},
    {'item': 'Batmobile',         'price': 10000000}
]

my_cart = ShoppingCart('Eric')

for item in shop_items:
    print(f"{item['item']}, ${item['price']:,.2f}\n")

def buy():
    while True:
        customer_choice = input('Please input your choice here: ')
        for item in shop_items:
            if customer_choice == str(item['item']):
                my_cart.add_item(item['item'], item['price'])
                print(ShoppingCart.items_in_cart)
                break