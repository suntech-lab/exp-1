"""
Review Exercise 4 GameDesign 12
Eric Liu
21/02/2025
"""

#1
print("""
EEEEEEE L
E       L
EEEEEEE L
E       L
EEEEEEE LLLLLLL
""")

#2
print("EEEEEEE L")
print("E       L")
print("EEEEEEE L")
print("E       L")
print("EEEEEEE LLLLLLL")

#3
lInitials = [
    "EEEEEEE L",
    "E       L",
    "EEEEEEE L",
    "E       L",
    "EEEEEEE LLLLLLL"
]

for line in lInitials:
    print(line)

#4
lE = [
    "EEEEEEE", 
    "E      ", 
    "EEEEEEE", 
    "E      ", 
    "EEEEEEE"
]

lL = [
    "L      ", 
    "L      ", 
    "L      ", 
    "L      ", 
    "LLLLLLL"
]

for lE, lL in zip(lE, lL):
    print(lE + "  " + lL)