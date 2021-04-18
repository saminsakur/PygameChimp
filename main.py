from pygame.locals import *
import pygame
import sys
import os

WidthHeight = 200, 300
running = True
screen = pygame.display.set_mode(WidthHeight)

if not pygame.font:
    print("Waring: fonts disabled")

if not pygame.mixer:
    print("Waring: media disabled")


def add_image(name, colorkey=None):
    FullName = os.path.join("data", name)
    try:
        image = pygame.image.load(FullName)
    except pygame.error as messege:
        print("The image cannot be shown:", name)
        raise SystemExit(messege)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        add_image()

    pygame.display.flip()
