'''
2048 GameDesign12 Project
Eric Liu
30/01/2025
'''

import random

board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 0, 0]
    ]

def Display(board):

    i = 0
    while i < len(board):
        print(board[i])
        i += 1

Display(board)