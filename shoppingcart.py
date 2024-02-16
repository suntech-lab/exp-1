class Dairy(object):
    def __init__(self):
        pass

    def desc(self):
        print('This product is dairy.')

class Frozen(object):
    def __init__(self):
        pass

    def desc(self):
        print('This product is frozen.')

class Vegetable(object):
    def __init__(self):
        pass

    def desc(self):
        print('This product is a vegetable.')

class Inedible(object):
    def __init__(self):
        pass

    def desc(self):
        print('This product is inedible. Very unfortunate.')

class ShoppingCart(object):

    items_in_cart = []

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def do_nothing():
        pass

    def add_item(self):

        for item in shop_items:
            print(f"press {item['opt']} for: {item['item']}, ${item['price']:,.2f}\n")

        user_opt_choice = input('\nPlease enter here: ')

        for opt in shop_items:
            if user_opt_choice == str(opt['opt']):

                self.items_in_cart.append({'item': opt['item'], 'price': opt['price'], 'weight': opt['weight']})
                print(f'{opt['item']} added.')
                break
        start()


    def remove_item(self):
        if len(self.items_in_cart) == 0:
            print('There is nothing in your cart.')
            start()

        for item in self.items_in_cart:
            print(f'{item['item']}, ${item['price']}, {item['weight']}kg')
        item_to_remove = input('Enter the name of the item you want to remove: ')

        for item in self.items_in_cart:
            if item_to_remove == str(item['item']):
                self.items_in_cart.remove(item)
                print(f'{item_to_remove} has been removed from your cart.')
                break
        start()

    def total(self):
        total = 0
        weight = 0
        for item in self.items_in_cart:
            total += item['price']
            weight += item['weight']
        print(f"The total value of the items in {self.customer_name}'s cart is ${total:,.2f} and it weighs a total of {weight:,.2f}")
        if total > 50:
            print('You are eligible for free shipping!')
        start()

    def check_cart(self):
        if len(self.items_in_cart) == 0:
            print('There is nothing in your cart.')

        else:
            for item in self.items_in_cart:
                print(f'{item['item']}, ${item['price']}, {item['weight']}kg')
            
        start()
        
    def coupon(self):
        have_coupon = input('Enter your coupon here: ')#???
        for coupon in coupons:                         #???
            if have_coupon == str(coupon['coupon']):   #???
                print('Coupon success.')               #???
            else:                                      #???
                print('Invalid coupon.')               #???
                self.proceed_to_checkout()             #???

    def proceed_to_checkout(self):
        notax = 0
        weight = 0
        if len(self.items_in_cart) == 0:
            print('There is nothing in your cart.')
        for item in self.items_in_cart:
            notax += item['price']
            weight += item['weight']
        for opt in coupon_menu:
            print(f'Press {opt['havecoupons']} if you {opt['desc']}.')

        coupon_menu_choice = input('Enter here: ')

        for opt in coupon_menu:
            if coupon_menu_choice == str(opt['havecoupons']):
                opt['func'](my_cart)

        else:
            pass
        
        if notax > 50:
            print(f'Your total with tax comes to {notax*0.05 + notax*0.07 + notax:,.2f}. Shipping is not included because you have spent over 50 dollars. Thank you for your patronage!')
        else:
            print(f'Your total with tax comes to {notax*0.05 + notax*0.07 + weight*2 + notax:,.2f}. Shipping fees were included because your purchase was not valued higher than 50 dollars. Thank you for your patronage!')
            

shop_items = [
    {'opt': 1,  'item': 'Milk',              'price':     3.99, 'weight':      4},
    {'opt': 2,  'item': 'Icecream',          'price':     5.99, 'weight':      4},
    {'opt': 3,  'item': 'Frozen Peas',       'price':      7.5, 'weight':    3.5},
    {'opt': 4,  'item': 'Sack of Potatoes',  'price':      5.5, 'weight':      6},
    {'opt': 5,  'item': 'Dr. Martens Boots', 'price':      212, 'weight':      1},
    {'opt': 6,  'item': 'Jellyfish Lamp',    'price':      8.1, 'weight':    1.5},
    {'opt': 7,  'item': 'Romance Novel',     'price':    10.25, 'weight':    0.7},
    {'opt': 8,  'item': '15 Pound Dumbells', 'price':     9.50, 'weight':   13.6},
    {'opt': 9,  'item': 'Headphones',        'price':     70.8, 'weight':    0.3},
    {'opt': 10, 'item': 'Batmobile',         'price':   150000, 'weight': 2494.8}
]

menu = [
    {'opt': 1, 'desc': 'add an item to the cart',          'func':            ShoppingCart.add_item},
    {'opt': 2, 'desc': 'remove an item from the cart',     'func':         ShoppingCart.remove_item},
    {'opt': 3, 'desc': 'find the total price of the cart', 'func':               ShoppingCart.total},
    {'opt': 4, 'desc': 'check the cart',                   'func':          ShoppingCart.check_cart},
    {'opt': 5, 'desc': 'checkout',                         'func': ShoppingCart.proceed_to_checkout}

]

coupon_menu = [
    {'havecoupons': 'y', 'desc':          'you have coupons', 'func':     ShoppingCart.coupon},
    {'havecoupons': 'n', 'desc': 'you dont have any coupons', 'func': ShoppingCart.do_nothing}
]

coupons = [
    {'coupon': 'thisisgreat.Extending!'},
    {'coupon':          'acouponthisis'}
]

def start():
    for opt in menu:
            print(f"press {opt['opt']} to {opt['desc']}")

    user_opt_choice = input('\nPlease enter here: ')

    for opt in menu:
        if user_opt_choice == str(opt['opt']):

            opt['func'](my_cart)
            break

my_cart = ShoppingCart('Eric')

start()