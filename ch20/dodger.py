# dodger.py
# Dodger
#   A simple graphical game where the
#   player must dosge the bad guys.
"""
The Dodger game has the player control
a small person (which we call the
player’s character) who must dodge
a whole bunch of baddies that fall
from the top of the screen. The
longer the player can keep dodging
the baddies, the higher the score they
will get.

An example from Chapter 20 of
'Invent Your Own Games With Python'
  by Al Sweigart

A.C. LoGreco
"""


import pygame, random, sys
from pygame.locals import *


WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()     # quit the game when escape key is pressed
                return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


