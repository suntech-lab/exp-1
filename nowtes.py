#Basic 'Built in' Function Demo

# Functions: small repeatable tasks placed elsewhere in the code
# that perform ONE SINGLE WELL DEFINED TASK

# the print function goes through quite a few steps to
# print the value on the screen. We send it an "argument" or
# "parameter" and like black box theory, it does all the magic
# for us. We can send it quite a few different arguements

print ('happy')     #<-- string type
print (32 * 2)      #<-- do some 'math' here
print (3.14159)     #<-- floats
print (True)        #<-- boolean True or False




print (int('32'))   #<-- you can even send some of them the results
print (int('32')*2) #   of other functions
#print (int('hello')) # this one is an error
print (int(3.9999)) # int FORCES an argument to be an integer type
                    # # this is known as type casting or type coercion


print (float('3.14159'))


# There are TONS of Predefined functions available.
# you just need to find one that does what you want
# and import the module

import math # NOTE: Never Never Never use an import stmnt
            # partway through a program like this BAAAAADDDDD!!! :)

print(math.pi)




from math import *    # Alternate way of importing
print(pi)             # Allows you to short form stmnts


# Demonstration of using functions for better code organization, modularity, reusability, and debugging

# Function to calculate the area of a rectangle
def AreaRectangle(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def PerimeterRectangle(length, width):
    return 2 * (length + width)

# Function to display information about a rectangle
def RectangleInfo(iLength, iWidth):
    print("Rectangle Information:")
    print("Length:", iLength)
    print("Width:", iWidth)
    print("Area:", AreaRectangle(iLength, iWidth))
    print("Perimeter:", PerimeterRectangle(iLength, iWidth))
    print()


# Define rectangle dimensions
Rect1Length = 5
Rect1Width = 3

Rect2Length = 7
Rect2Width = 4


# Display information about rectangle 1
RectangleInfo(Rect1Length, Rect1Width)

# Display information about rectangle 2
RectangleInfo(Rect2Length, Rect2Width)



# Fruitful functions return. 


'''
Day 1B
Programmer Defined Functions

1. Describle what a function is
	Code that tells the computer what to do
2. What are the X and Y called in the following:
			functionname (X,Y)
3. What is a fruitful function? Non fruitful?
	Fruitful has a return statement (returns a value when called)
4. How can you use code from other bits of python?
	Import module
'''


# Programmer Defined Functions
# As mentioned yesterday, functions are 
# blocks of code that do a single well defined
# task. Add tax or create a message or W.H.Y.



'''
Functions Notes:
The function definition must appear in the code
before the function call in Python. Other languages
not so much. By blake convention, put them at the 
top of the code after any imports, global 
var, and setup
'''

# Sample Void Functions with and without 
# Void functions do not have a return statment
# also called on-fruitful functions
# arguments/parameters
# This particular function is as simple as it gets
# We have named this short code block fHelloWorld
# It doesn't need anything to do its job (no arguments/parameters)

def fHelloWorld():
	print("Hello World")

# definition above. Note the syntax of the layout
# when the code gets run, the computer reads but does not execute
# the above NAMED CODEBLOCK. 
# Later in the program we can then use that named block and call up
# that code to do whatever it is designed to do.
fHelloWorld() 

# Here is a similar example but we are sending it some data or values
# Again this is a void function. But we send it two values
# The order that the values are presented in the call, is the order
# they get stored in the definition. Consider these sObject1 and sObject2
# to be variables. The values in the call stmnt get stored there.
def fMrBlakesTruth(sObject1, sObject2):
	print (sObject1, " ", sObject2)
	print ("{0} is better than {1} ".format(sObject1, sObject2))
	

# call the function repeatedly and send it different arguments to process
fMrBlakesTruth('Android', 'Apple iOS')
fMrBlakesTruth('Vanilla Icecream', 'Chocolate Icecream')



# Sample Fruitful Functions
# Fruitful functions are ones that use a return statement
def fFormatDecimal(fUglyDecimalValue):
	return ('%1.2f' %fUglyDecimalValue)

print(fFormatDecimal(3.14159))



# Exercise: create a fruitful python function to
# return a formatted dollar amount to be printed
# Argument: 12.666666
# Return: "$12.67"



# Exercise
def fFormatDollar(fAmount):
	return ('%1.2f' %fAmount)

print('$' + str(fFormatDollar(12.66666)))

