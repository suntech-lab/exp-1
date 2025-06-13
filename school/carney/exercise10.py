def valid_triangle(straw1, straw2, straw3):
    if straw1 >= straw2 + straw3:
        print('False')
    elif straw2 >= straw3 + straw1:
        print('False')
    elif straw3 >= straw1 + straw2:
        print('False')
    else:
        print('True')

straw1 = int(input('what is the length of the first straw: '))
straw2 = int(input('what is the length of the second straw: '))
straw3 = int(input('what is the length of the third straw: '))

valid_triangle(straw1, straw2, straw3)