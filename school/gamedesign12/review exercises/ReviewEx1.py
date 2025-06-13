"""
Review Exercise 1 GameDesign 12
Eric Liu
21/02/2025
"""

iSize = 5
lFirstRow = [str(i) for i in range(1, iSize + 1)]
lFirstColumn = [str(i) for i in range(1, iSize + 1)]

table = [[" "] + lFirstRow]

for y in range(iSize):
    row = [lFirstColumn[y]]
    for x in range(iSize):
        row.append(str(int(lFirstColumn[y]) * int(lFirstRow[x])))
    table.append(row)

j = 0
while j < len(table):

    i = 0
    row = ""
    while i < len(table[j]):
        row += f'{table[j][i]:4}'
        i += 1
    print(row)
    j += 1