import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           new_rad = self.radius - ASTEROID_MIN_RADIUS
           random_angle = random.uniform(20, 50)
           top_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
           top_asteroid.velocity = (self.velocity.rotate(random_angle) * 1.2)
           bottom_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
           bottom_asteroid.velocity = (self.velocity.rotate(-random_angle) * 1.2)
           
