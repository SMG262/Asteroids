import pygame
from pygame import draw
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def turn_speed(self, dt):
        pass

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
        # For left rotation, reverse dt (make it negative)
            self.rotate(-dt)  # or self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
        # For right rotation
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt) 
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if self.timer > 0:
            self.timer -= dt
        else: self.timer = 0
        
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer += PLAYER_SHOOT_COOLDOWN
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, velocity)