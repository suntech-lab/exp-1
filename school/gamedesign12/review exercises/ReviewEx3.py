"""
Review Exercise 3 GameDesign 12
Eric Liu
21/02/2025
"""
iPennies = 93

iQuarters, iPennies = divmod(iPennies, 25)
iDimes, iPennies = divmod(iPennies, 10)
iNickels, iPennies = divmod(iPennies, 5)

print(iQuarters)
print(iDimes)
print(iNickels)
print(iPennies)