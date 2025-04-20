import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS



class Shot(CircleShape, pygame.sprite.Sprite):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt