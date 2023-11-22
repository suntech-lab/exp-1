BC_TAX = 0.07
TIP = 0.12
meal = float(input('enter the price of your meal and this will calculate the tax and tip: '))
meal_tax = (meal * BC_TAX)
meal_tip = (meal * TIP)
meal_total = (meal * BC_TAX + meal * TIP)
print(f'your tip for this meal is ${meal_tip:.2f}, your tax for this meal is ${meal_tax:.2f}, and your total is ${meal_total:.2f}.')
