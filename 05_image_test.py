""" 05_image_test.py """

import sys
import pygame
from pygame.locals import QUIT

SURFACE_WIDTH = 400
SURFACE_HIGHT = 300

pygame.init()
SURFACE = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HIGHT))
FPSCLOCK = pygame.time.Clock()

def main():
    """main routine"""
    logo = pygame.image.load("pygame-logo.jpg")

    character_x = SURFACE_WIDTH//2 - 270//2
    character_y = SURFACE_HIGHT//2 - 187//2

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SURFACE.fill((255, 255, 255))
        SURFACE.blit(logo, (character_x, character_y))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()