import sys

import pygame

import asteroidfield
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            collision = asteroid.check_collisions(player)
            if collision:
                print("Game Over!")
                sys.exit()
            for shot in shots:
                collision = asteroid.check_collisions(shot)
                if collision:
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
