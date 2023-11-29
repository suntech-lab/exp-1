import cmath

a = float(input('enter a: '))

if a == 0:
    print('a may not be zero')

b = float(input('enter b: '))
c = float(input('enter c: '))

print(a,'* x^2', '+', b,'* x', '+', c)

# i couldnt find a way of using/evaluating plus minus in python without downloading something
def quadratic_solver(a, b, c):

    d = (b**2) - (4*a*c)

    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)

    if root1 == root2:

        return root1
    
    return root1, root2

print(quadratic_solver(a, b, c))
