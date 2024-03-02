def trianglemaker(rows):
    numberofrows = 0
    asterisksperrow = 1
    while numberofrows < rows:
        print('*'*asterisksperrow)
        numberofrows += 1
        asterisksperrow += 1

rows = int(input('How many rows do you want for your right angled triangle?: '))

trianglemaker(rows)
