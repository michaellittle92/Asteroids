from constants import * 
import pygame
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    clock.tick()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    player = Player(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick()/1000
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()