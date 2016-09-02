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
