"""
Review Exercise 7 GameDesign 12
Eric Liu
23/02/2025
"""

iFirstPoint = int(input('enter the first point: '))
iSecondPoint = int(input('enter the second point: '))

if iFirstPoint < iSecondPoint:
    iStartPoint = iFirstPoint
    iEndPoint = iSecondPoint
else:
    iStartPoint = iSecondPoint
    iEndPoint = iFirstPoint

total = 0
for n in range(iStartPoint, iEndPoint + 1):
    total += n

print(total)