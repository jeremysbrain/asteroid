import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    
    
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collision(p):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(color="black")
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()