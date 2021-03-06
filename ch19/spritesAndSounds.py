# spritesAndSounds.py
# Collision Detection
#   with Keyboard and Mouse Input
#   and with spites and sounds
"""
This is a demonstration of doing
collison detection with pygame.
This also demonstrates how to get user
input from the keyboard and the mouse
using pygame. The use of Sprites,
sound, and music are demonstrated as
well.

An example from Chapter 19 of
'Invent Your Own Games With Python'
  by Al Sweigart

A.C. LoGreco
"""

import pygame, sys, time, random, os
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sound')

# set up the colors
BLACK = (0, 0, 0)

# set up the block data structure
# player
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load(os.path.join('sprites', 'player.png'))
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
# food
foodImage = pygame.image.load(os.path.join('sprites', 'cherry.png'))
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20),
                             random.randint(0, WINDOWHEIGHT - 20), 20, 20))

foodCounter = 0
NEWFOOD = 40

# set up keyboard flags
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# set up music
pickUpSound = pygame.mixer.Sound(file='./sounds/pickup.wav')
pickUpSound.set_volume(0.3)
pygame.mixer.music.load('./sounds/background.mid')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# The main game loop
while True:
    # event loop
    for event in pygame.event.get():
        # check for the QUIT event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard flags
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
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10,
                                     20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0  # reset food counter
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20),
                                 random.randint(0, WINDOWHEIGHT - 20),
                                 20, 20))

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # draw the player's sprite onto the surface
    windowSurface.blit(playerStretchedImage, player)

    # check if the player's bounding block has
    # intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top,
                                 player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage,
                                                          (player.width,
                                                           player.height))
            if musicPlaying:
                pickUpSound.play()

    # draw the food
    for food in foods:
        windowSurface.blit(foodImage, food)

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
