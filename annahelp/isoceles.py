def isosceles(rows):
    numberofrows = 0
    asterisksperrow = 1
    spacesperrow = rows
    while numberofrows < rows:
        print(f' '*spacesperrow + '*'*asterisksperrow)
        numberofrows += 1
        asterisksperrow += 2
        spacesperrow -= 1

rows = int(input('How many rows do you want for your isosceles triangle?: '))

isosceles(rows)