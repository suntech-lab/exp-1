posint = int(input('enter a positive integer: '))
sum = 0
if posint <= 0:
    print('not a positive integer')
for n in range(0, posint):
    sum += n**3
print(sum)