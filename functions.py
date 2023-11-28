import math
import requests

def request(site, a, b):
    while a < b:
        requests.get(site)
        a += 1
        print('a')
    return requests.get(site)

def circle_area(r):
    areaC = math.pi * r ** 2
    return areaC

def square_area(side_length):
    areaS = side_length**2
    return areaS

r = float(input('enter the radius of your circle: '))
print(circle_area(r))

side_length = float(input('enter the side length of your square: '))
print(square_area(side_length))

site = str(input('what site do you want to get: '))
b = int(input('how many times do you want to talk to this site: '))
a = 0
print(request(site, a, b))