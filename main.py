import pygame
import player
from constants import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    draw_player = player.Player(x, y)

    while True:
        dt = timer.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        draw_player.update(dt)
        
        screen.fill('black')
        draw_player.draw(screen)
        pygame.display.flip()
        
        
    
    
if __name__ == "__main__":
    main()
    