import cmath

a = float(input('enter a: '))

while a == 0:
    print('A may not be zero. Try again.')
    a = float(input('enter a: '))

b = float(input('enter b: '))
c = float(input('enter c: '))

print('Standard Quadratic Form:', a,'* x^2', '+', b,'* x', '+', c)

def quadratic_solver(a, b, c):

    d = b**2 - 4*a*c

    # i couldnt find a way of using/evaluating plus minus in python without downloading something
    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)

    if root1 == root2:

        return root1
    
    return root1, root2

print('Root(s):', quadratic_solver(a, b, c))