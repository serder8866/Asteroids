import pygame
import sys
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    print(type(screen))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for item in asteroids:
            for bullet in shots:
                if item.collides_with(bullet):
                    log_event("asteroid_shot")
                    item.split()
                    bullet.kill()
        for group in drawable:
            group.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
