import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    display = pygame.display.set_mode((1280, 720), 0, 32)

    white = (255,255,255)
    blue = (0,0,255)

    display.fill(white)

    pygame.draw.rect(display, blue, (0, 0, 100, 100))

    running = 1;
    while running == 1:
        for event in pygame.event.get():
            if event.type == quit:
                running = 0;
                pygame.quit()
                sys.exit()
                
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            running = 0;

        pygame.display.update();

main()