base = int(input('define base: '))
exponent = int(input('define exponent: '))

def power(base, exponent):
    if base == 1 or exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(power(base, exponent))