import random
list = []
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""
Pre: 
    1.) the function takes the list, list and the list, numbers
    2.) the function appends random numbers from one to ten until the length of the list reaches one hundred thousand
    3.) it uses a for loop to keep track of how many times it has appeared by adding one to the index that is the difference between the number and one
    4.) uses the x variable to keep track of the number that appears
    5.) takes the value of the index of the difference between x and one to print the amount of times that it appeared
    6.) adds one to x

post:
    it just works
"""


def get_stats():
    x = 1
    while len(list) < 100000:
        list.append(random.randint(1,10))

    for number in list:
        numbers[number - 1] += 1

    for number in numbers:
        print(f'{x} appeared {numbers[x - 1]} times')
        x += 1

get_stats()