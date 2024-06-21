from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result


numbers = range(1, 21)
result = lcm_multiple(numbers)
print(result)