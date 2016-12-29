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


# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible('False')

# set up fonts
font = pygame.font.SysFont(None, 48)

# set up sounds
gameOverSound = pygame.mixer.Sound(file='./sounds/gameover.wav')
gameOverSound.set_volume(0.3)
pygame.mixer.music.load('./sounds/background.mid')
pygame.mixer.music.set_volume(0.1)

# set up images
playerImage = player.image.load(os.path.join('sprites', 'player.png'))
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load(os.path.join('sprites', 'baddie.png'))

# show the "Start" screen
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface,
         (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


topScore = 0
while True:
    # set up the start of the game
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:     # the game loop runs while the game part is playing
        score += 1  # increase the score

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or evemt.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type = MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                playerRect.move_ip(event.pos[0] - playerRect.centerx,
                                   event.pos[1] - playerRect.centery)

        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect':
                         pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize),
                                     0 - baddieSize,
                                     baddieSize,
                                     baddieSize),
                         'speed': 
                         random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface':
                         pygame.transform.scale(baddieImage,
                                                (baddieSize, baddieSize)),
                         }
            baddies.append(newBaddie)

        
