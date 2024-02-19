class ShoppingCart(object):

    items_in_cart = [] #list with items as dictionaries

    coupon_discount = 1 #discount multiplier

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def do_nothing(self): 
        pass

    def add_item(self):
        print('\n')
        saw_item = False

        for item in shop_items: #show the shop
            print(f"press {item['opt']} for: {item['item']}, ${item['price']:,.2f}")

        user_opt_choice = input('\nPlease enter here: ')

        while saw_item == False: #if python has not seen the item that the user wants to add to cart

            for opt in shop_items:

                if user_opt_choice == str(opt['opt']): #if python finds the item
                    saw_item = True

                    for item in self.items_in_cart:

                        if str(opt['item']) == item['item']: #if the item is already in the cart
                            print(f"This item is already in {self.customer_name}'s cart.")
                            start()

                    else: #if its not in cart already
                        self.items_in_cart.append({'item': opt['item'], 'price': opt['price'], 'weight': opt['weight']})
                        print(f"{opt['item']} added to {self.customer_name}'s cart.")
                        break

            else: #incase the user enters something wrong
                print('Invalid input. Maybe you meant to input a number?')

            start()


    def remove_item(self):
        print('\n')
        saw_item = False

        if len(self.items_in_cart) == 0:
            print('There is nothing in your cart.')
            start()

        for item in self.items_in_cart: #print cart
            print(f"{item['item']}, ${item['price']}, {item['weight']}kg")

        item_to_remove = input('Enter the name of the item you want to remove: ')

        while saw_item == False: #same logic with add_item

            for item in self.items_in_cart:

                if item_to_remove == str(item['item']):
                    saw_item = True
                    self.items_in_cart.remove(item)
                    print(f"{item_to_remove} has been removed from {self.customer_name}'s cart.")
                    break

            else:
                print('Invalid input. Maybe you spelt something wrong?')

            start()

    def total(self):
        total = 0
        weight = 0 #weight is for shipping

        for item in self.items_in_cart: #add everything up
            total += item['price']
            weight += item['weight']

        print(f"The total value of the items in {self.customer_name}'s cart is ${total:,.2f} and it weighs a total of {weight:,.2f} kilograms.")
        
        if total > 50:
            print('You are eligible for free shipping!')

        start()

    def check_cart(self):

        if len(self.items_in_cart) == 0:
            print(f"There is nothing in {self.customer_name}'s cart.")

        else:

            for item in self.items_in_cart: #print contents of cart
                print(f"{item['item']}, ${item['price']}, {item['weight']}kg")
            
        start()
   
    def coupon(self):
        print('\n')
        saw_coupon = False
        have_coupon = input('Enter your coupon here: ')

        while saw_coupon == False: #same logic as add_item

            for dict in discount:

                if have_coupon == dict['coupon']:
                    print('Coupon success.')
                    self.coupon_discount = 0.5 #change the discount multiplier to 50% off
                    saw_coupon = True
                    break

            else:
                print('Coupon invalid.')
                self.proceed_to_checkout()


    def proceed_to_checkout(self):
        print('\n')
        notax = 0 #cost before tax
        weight = 0

        if len(self.items_in_cart) == 0:
            print(f"There is nothing in {self.customer_name}'s cart.")

        for item in self.items_in_cart:
            notax += item['price']
            weight += item['weight']

        for opt in coupon_menu: #ask of the user has coupons
            print(f"Press {opt['havecoupons']} if you {opt['desc']}.")

        coupon_menu_choice = input('Enter here: ')

        for opt in coupon_menu:

            if coupon_menu_choice == str(opt['havecoupons']):
                opt['func'](my_cart)

        else:

            pass
        
        if notax > 50:
            print(f"{self.customer_name}'s total with tax comes to {notax*0.05 + notax*0.07 + notax*self.coupon_discount:,.2f}. Shipping is not included because you have spent over 50 dollars. Thank you for your patronage!")
            exit()

        else: #add shpping costs if the cart is worth less than 50$
            print(f"{self.customer_name}'s total with tax comes to {notax*0.05 + notax*0.07 + weight*1.25 + notax*self.coupon_discount:,.2f}. Shipping fees were included because your purchase was not valued higher than 50 dollars. Thank you for your patronage!")
            exit()

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

discount = [
    {'coupon': 'thisisgreat.Extending!'},
    {'coupon':          'acouponthisis'}
    ]

def start():
    print('\n')

    for opt in menu:
            print(f"press {opt['opt']} to {opt['desc']}")

    user_opt_choice = input('\nPlease enter here: ')

    for opt in menu:

        if user_opt_choice == str(opt['opt']):
            opt['func'](my_cart)
            break

my_cart = ShoppingCart('Eric') #initialize

start()