import pygame

from constants import *
from player import *

def main():
    pygame.get_init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")

        p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        p.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()