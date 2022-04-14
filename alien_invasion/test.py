import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800), 0)
screen.fill((240, 240, 240))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
