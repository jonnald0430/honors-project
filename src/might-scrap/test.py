import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Suction Simulation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class BlackHole:
    G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
    C = 299792458.0  # Speed of light (m/s)

    def __init__(self, x, y, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), self.radius)

    def gravity_force(self, obj):
        # Calculate distance between the object and the black hole
        distance_x = self.x - obj.x
        distance_y = self.y - obj.y
        distance_squared = distance_x ** 2 + distance_y ** 2
        distance = math.sqrt(distance_squared)

        # Calculate the force magnitude using the Schwarzschild metric
        force_magnitude = self.G * self.mass / distance_squared

        # Calculate the force direction
        force_x = force_magnitude * (distance_x / distance)
        force_y = force_magnitude * (distance_y / distance)

        return force_x, force_y


class Object:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)

    def update_position(self, force_x, force_y):
        # Update velocity using Newton's second law
        self.x_vel += force_x / self.mass
        self.y_vel += force_y / self.mass

        # Update position using velocity
        self.x += self.x_vel
        self.y += self.y_vel


def main():
    run = True
    clock = pygame.time.Clock()

    black_hole = BlackHole(0, 0, 20, 10**6)  # Schwarzschild black hole
    obj = Object(-400, 0, 10, (0, 255, 255), 10**3)  # Initial position and properties of the object

    while run:
        clock.tick(60)
        WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Calculate gravitational force exerted by the black hole
        force_x, force_y = black_hole.gravity_force(obj)

        # Update object's position based on gravitational force
        obj.update_position(force_x, force_y)

        # Draw the black hole and the object
        black_hole.draw(WIN)
        obj.draw(WIN)

        # Check if the object crosses the event horizon (for visualization purposes)
        if math.sqrt((obj.x - black_hole.x) ** 2 + (obj.y - black_hole.y) ** 2) < black_hole.radius:
            print("Object crossed event horizon!")
            run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()