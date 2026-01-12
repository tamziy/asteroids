from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, SHOT_LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # i need to know where to get position and radius or where it comes from
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_LINE_WIDTH) 

    def update(self, dt):
        self.position += (self.velocity * dt)
        