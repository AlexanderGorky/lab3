# рисование в pygame
import pygame
from pygame.draw import *

def fish(x, y, angle, scale):
    """
    draws a fish with x, y coordinates rotated by an angle relative to the vertical at scale
    """
    print("рисую рыбу")
    pass

def cat (x, y, color, scale):
    """
    draws a cat with x, y coordinates in a certain color at scale
    """
    print("рисую кошку")
    pass

pygame.init()

FPS = 30
screen_size = (400, 400)
screen = pygame.display.set_mode((screen_size))

screen_color = (192, 192, 192)

cat (0, 0, (0, 0, 0), 2)
fish (0, 0, (0, 0, 0), 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()