""" 02_draw_rect.py """

import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        SURFACE.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.draw.rect(SURFACE, (0,0,0), (100, 100, 50, 50), 0, 10)
        
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()