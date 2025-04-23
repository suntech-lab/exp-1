"""
Game Design 12, Snakes and Ladders Practical
Eric Liu
17/04/2025
"""

def fGetTilePosition(TileNumber):
    #pre: needs the number of the tile in question
    #post: returns the tile number and coordinated of top left pixel in a tuple

    iRow = (TileNumber - 1) // 10 + 1 #-1 because i need to differentiate between rows that start with consequtive numbers
    
    if iRow % 2 == 1:
        iCol = (TileNumber - 1) % 10 + 1
    else:
        iCol = 10 - ((TileNumber - 1) % 10) #100 has coords (1, 1) and 1 has coords (1, 451), so its 10- for the iRow
    
    XLoc = 1 + (iCol - 1) * 50
    YLoc = 451 - (iRow - 1) * 50
    
    return (TileNumber, XLoc, YLoc)

print(fGetTilePosition(61))
print(fGetTilePosition(77))
print(fGetTilePosition(12))
print(fGetTilePosition(38))