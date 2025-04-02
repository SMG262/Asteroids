import pygame
from constants import SHOT_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.alive = True

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        screen_width, screen_height = SCREEN_WIDTH, SCREEN_HEIGHT  
        if (self.position.x < 0 or self.position.x > screen_width or
            self.position.y < 0 or self.position.y > screen_height):
            self.kill()