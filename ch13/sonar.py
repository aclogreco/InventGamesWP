# sonar.py
"""
Sonar - an open seas treasure hunt game
An example from Chapter 13 of 
'Invent Your Own Games With Python' by Al Sweigart
A.C. LoGreco
"""

import random
import sys


def drawBoard(board):
    """
    Draw the board data structure.
    """

    hline = '     '  # initial space for the numbers
                     # down the left side of the board
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


def getNewBoard():
    """
    Create a new 60x15 board data structure.
    """
    board = []
    for x in range(60):  # the main list is a list of 60 lists
        board.append([])
        for y in range(15):  # each list in the main list
                             # has 15 single-character strings
            # use different characters for the ocean to make it more readable
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def getRandomChests(numChests):
    """
    Create a list of chest data structures
    (two-item  lists of x, y int coordinates).
    """
    chests = []
    for i in range(numChests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    return chests


def isValidMove(x, y):
    """
    Return True if the coordinates are on the board, otherwise False.
    """
    return x >= 0 and x <= 59 and y >= 0 and y <= 14


def makeMove(board, chests, x, y):
    """
    Change the board data structure with a sonar device character. Remove 
    treasure chests from the chests list as they are found. Return False if 
    this an invalid move. Otherwise, return the string of the result of this 
    move.
    """
    if not isValidMove(x, y):
        return False
    
    smallestDistance = 100  # any chest will be closer than 100.
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        
        if distance < smallestDistance:  # we want the closest treasure chest.
            smallestDistance = distance
    
    if smallestDistance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            result = 'Treasure detected at a distance of '
            result += '%s from the sonar device.' % (smallestDistance)
            return result
        else:
            board[x][y] = 'O'
            result = 'Sonar did not detect anything. '
            result += 'All treasure chests out of range.'
            return result


def enterPlayerMove():
    """
    Let the player type in their move. Return a two-item list of int xy 
    coordinates.
    """
    print(
        'Where do you want to drop the next sonar device? ' + 
        '(0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
        
        move = move.split()
        if (len(move) == 2 and move[0].isdigit() and move[1].isdigit() and 
                isValidMove(int(move[0]), int(move[1]))):
            return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59, a space, ' + 
            'then a number from 0 to 14.')


