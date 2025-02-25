"""
Review Exercise 8 GameDesign 12
Eric Liu
23/02/2025
"""

fBalance = float(input('whats the current balance?: '))
fEndBalance = fBalance * 2
fInterest = float(input('whats the compound interest rate?: '))

iYears = 0
while fBalance < fEndBalance:
    fBalance = fBalance * fInterest
    iYears += 1

print(f'its gonna take {iYears} years')