# reversi.py
# Reversi (Othello)
"""
Reversi - a tile flipping game
An example from Chapter 15 of 
'Invent Your Own Games With Python' by Al Sweigart
A.C. LoGreco
"""

import random
import sys


def drawBoard(board):
    """
    This function prints out the board that it was passed. Returns None.
    """
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)


def resetBoard(board):
    """
    Blanks out the board it is passed, except for the original starting position.
    """
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    # Starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():
    """
    Creates a brand new, blank board data structure.
    """
    board = []
    
    for i in range(8):
        board.append([' '] * 8)

    return board



