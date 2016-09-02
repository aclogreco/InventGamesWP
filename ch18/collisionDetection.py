# collisionDetection.py
# Collision Detection
"""
This is a demonstration of doing collison detection with pygame.
An example from Chapter 18 of
'Invent Your Own Games With Python' by Al Sweigart

A.C. LoGreco
"""

import pygame, sys, random
from pygame.locals import *


def doRectsOverlap(rect1, rect2):
    """
    This function checks if two rectangles overlap.
    Returns TRUE if they do and FALSE if they do not.
    """
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or 
            (isPointInsideRect(a.left, a.bottom, b)) or 
            (isPointInsideRect(a.right, a.top, b)) or 
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

def isPointInsideRect(x, y, rect):
    """
    This function determines if the point x, y is within the rectangle rect.
    Returns TRUE if it is and FALSE if it is not.
    """
    if ((x > rect.left) and
        (x < rect.right) and
        (y > rect.top) and
        (y < rect.bottom)):
        return True
    else:
        return False


# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Collision Detection')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# set up the bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT}
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                             random.randint(0, WINDOWHEIGHT - FOODSIZE),
                             FOODSIZE, FOODSIZE))


