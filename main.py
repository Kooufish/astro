import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
    pygame.init()
    pygame.display.set_caption('Asteroids')

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0
    counter = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    spaceship = Player(x, y)
    AsteroidField()
    

    while True:
        dt = timer.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        updatable.update(dt)

        for asteroid in asteroids:
            if Player.collision(spaceship, asteroid):
                print("Game Over")
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if Player.collision(shot, asteroid):
                    shot.kill()
                    asteroid.split()
                    counter += 1
                    print(counter)


        screen.fill('black')
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()  
    
if __name__ == "__main__":
    main()
    