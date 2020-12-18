""" 06_move_image.py """

import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT

SURFACE_WIDTH = 400
SURFACE_HIGHT = 300

pygame.init()
SURFACE = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HIGHT))
FPSCLOCK = pygame.time.Clock()
pygame.key.set_repeat(10, 30)

def main():
    logo = pygame.image.load("pygame-logo.jpg")

    character_x = SURFACE_WIDTH//2 - 270//2
    character_y = SURFACE_HIGHT//2 - 187//2

    movement = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    movement = movement - 10
                elif event.key == K_RIGHT:
                    movement = movement + 10
        
        SURFACE.fill((255, 255, 255))
        SURFACE.blit(logo, (character_x + movement, character_y))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()