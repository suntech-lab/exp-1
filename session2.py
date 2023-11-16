num1 = int(input("Enter the first number: "))

def factorial(int):
    x = 1
    while num1 > 0:
        fact = (num1 - x) * num1
    x += 1
    return fact

op = str(input("Enter the operation: "))

if op == "factorial":
    print(num1, "factorial is ", factorial(num1))

num2 = int(input("Enter the second number: "))

if op == "+":
    print(num1, "+", num2, "is", num1 + num2)
if op == "-":       
    print(num1, "-", num2, "is", num1 - num2)
if op == "/":
    print(num1, "/", num2, "is", num1 / num2)
if op == "*":
    print(num1, "*", num2, "is", num1 * num2)
if op == "%":
    print(num1, "%", num2, "is", num1 % num2)
if op == "//":
    print(num1, "//", num2, "is", num1 // num2)
if op == "**":
    print(num1, "**", num2, "is", num1 ** num2)

