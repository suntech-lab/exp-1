num1 = int(input("Enter the first number: "))
op = str(input("Enter the operation: "))
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
