import random
n = str(input('What is your choice?:'))
i = random.randint(1,4)
if i == 1:
    print('i choose rock')
if i == 2:
    print('i choose paper')
if i == 3:
    print('i choose scissors')

if n == 'rock':
    if i == 1:
        print('tie')
    if i == 2:
        print('you lose')
    if i == 3:
        print('you win')
if n == 'paper':
    if i == 1:
        print('you win')
    if i == 2:
        print('tie')
    if i == 3:
        print('you lose')
if n == 'scissors':
    if i == 1:
        print('you lose')
    if i == 2:
        print('you win')
    if i == 3:
        print('tie')
