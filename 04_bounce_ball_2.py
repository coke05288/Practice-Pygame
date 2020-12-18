""" 04_bounce_ball_2.py """

import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    y = 0
    speed = 1
    gravity = 0.9
    while True:
        SURFACE.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        y = y + speed
        speed = speed + gravity

        if y > 300:
            speed = speed * -0.9
            y = 300

        pygame.draw.circle(SURFACE, (0,0,0), (200, y), 20, 5)
        
        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()