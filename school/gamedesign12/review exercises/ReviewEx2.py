"""
Review Exercise 2 GameDesign 12
Eric Liu
21/02/2025
"""

import math
tPointA = (2, 3)
tPointB = (5, 7)

fPointDistance = math.sqrt(math.pow((tPointA[0] - tPointB[0]), 2) + math.pow((tPointA[1] - tPointB[1]), 2))

print(fPointDistance)

'''
If the two points were the center of circles, and I wanted to know if they were colliding,
I would look at the sum of the radius of each circle and see if it is larger than OR EQUAL to
the distance between the center points.

I am looking at if it is equal to the distance between
the points as well because I want to know if they are touching too.

iRadiusA = 3
iRadiusB = 2
if iRadiusA + iRadiusB >= fPointDistance:
    print('the circles are colliding')
else:
    print('the circles are not colliding')

'''