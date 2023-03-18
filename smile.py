import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_size = (400, 400)
screen = pygame.display.set_mode((screen_size))

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
screen_color = (192, 192, 192)

screen.fill(screen_color)
circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 1)
circle(screen, red, (150, 180), 20)
circle(screen, black, (150, 180), 20, 1)
circle(screen, black, (150, 180), 9)
circle(screen, red, (250, 180), 15)
circle(screen, black, (250, 180), 15, 1)
circle(screen, black, (250, 180), 7)
rect(screen, black, (150, 250, 100, 20))
polygon(screen, black, [(100, 130), (180, 175), (186, 165), (106, 120), (100, 130)])
polygon(screen, black, [(220,175), (300,145), (297, 137), (217, 167), (220,175)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()