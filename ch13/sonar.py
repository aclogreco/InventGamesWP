# sonar.py
#
# Sonar - an open seas treasure hunt game
# A.C. LoGreco

import random
import sys

def drawBoard(board):
    """
    Draw the board data structure.
    """

    hline = '     '  # initial space for the numbers down the left side of the board
    for i in range(1, 6):
        hline += (' ' * 9) + str(i)

    # print the numbers across the top
    print(hline)
    print('   ' + ('0123456789' * 6))
    print()

    # print each of the 15 rows
    for i in range(15):
        # single-digit numbers need to be padded with an extra space
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('%s%s %s %s' % (extraSpace, i, getRow(board, i), i))

    # print the numbers across the bottom
    print()
    print('   ' + ('0123456789' * 6))
    print(hline)

def getRow(board, row):
    """
    Return a string from the board data structure at a certain row.
    """
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow


