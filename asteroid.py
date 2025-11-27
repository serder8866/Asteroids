from constants import *
from circleshape import CircleShape
import pygame
from logger import log_event
import random as r

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = r.uniform(20, 50)
            direction_1 = self.velocity.rotate(angle)
            direction_2 = self.velocity.rotate(-angle)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, smaller_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, smaller_radius)
            new_asteroid_1.velocity = direction_1 * 1.2
            new_asteroid_2.velocity = direction_2 * 1.2
            