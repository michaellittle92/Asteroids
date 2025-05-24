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

    updateable =  pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick()/1000
        screen.fill("black")

        for item in updateable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
    
        pygame.display.flip()
        

if __name__ == "__main__":
    main()