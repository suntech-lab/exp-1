BC_TAX = 0.07
TIP = 0.12
meal_price = float(input('enter the price of your meal and this will calculate the tax and tip: '))
meal_tax = (meal_price * BC_TAX)
meal_tip = (meal_price * TIP)
meal_total = (meal_price * BC_TAX + meal_price * TIP)
print(f'your tip for this meal is ${meal_tip:.2f}, your tax for this meal is ${meal_tax:.2f}, and your total is ${meal_total:.2f}.')
