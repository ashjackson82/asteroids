# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import CircleShape
from pygame.locals import *
from vfx import Explosion

def main():
    # Game initialization
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    explosion_group = pygame.sprite.Group()


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                sys.exit("Game Over!")
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot) == True:
                    pygame.sprite.Sprite.kill(shot)
                    exp = Explosion(asteroid.position.x,asteroid.position.y)
                    explosion_group.add(exp)
                    asteroid.split()

        screen.fill((5,5,5))
        for obj in drawable:
            obj.draw(screen)
        explosion_group.draw(screen)
        explosion_group.update()   
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()