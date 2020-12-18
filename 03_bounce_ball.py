""" 03_bounce_ball.py """

import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    y = 0
    speed = 10
    while True:
        SURFACE.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        y = y + speed

        if y > 300 or y < 0:
            speed = speed * -1

        pygame.draw.circle(SURFACE, (0,0,0), (200, y), 20, 5)
        
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()