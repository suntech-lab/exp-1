x=int(input('what is your lower limit: '))
y=int(input('what is your upper limit: '))
def sigma(x,y):
    if y==x:
        return y
    return y*sigma(x,y-1)
print(sigma(x,y))
