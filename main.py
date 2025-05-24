from constants import * 
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    clock.tick()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable =  pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)

    player = Player(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)
    asteroid_field = AsteroidField()
    
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