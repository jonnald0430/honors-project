import pygame
import math

pygame.init()

WIDTH, HEIGHT =  800, 800 # pixel resolution
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # window size
pygame.display.set_caption("Black Hole Simulaton") # window name

# planet colors
WHITE = (255, 255, 255) 
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("arial", 16)

class Planet:
	AU = 149.6e6 * 1000 # astronomical units in meters
	G = 6.67428e-11 # gravitational constant, is used to find the force of attraction between objects (in this case our Planets) 
	SCALE = 250 / AU  # 1AU = 100 pixels, scale for the PyGame window
	TIMESTEP = 3600*24 # represents 1 day
	
	def __init__(self, x, y, radius, color, mass):
		''' Initializes/sets up Planet objects for their movement around the sun, and their appearance.

	args: 
		x:
			Movement of Planet objects in the x-direction on screen.
		y: 
			Movement of Planet objects in the y-direction on screen.
		radius:
			The radius of each planet in this class.
		color: 
			The color of each planet in this class.
		mass:
			The mass of each planet in this class.

	returns:
		Planet objects in window.
		'''
		# the number of meters away from the Sun
		self.x = x 
		self.y = y
		# the radius of each Planet object
		self.radius = radius 

		self.color = color
		self.mass = mass # in kilograms, this is used to calculate the attraction between different planets, and create circular orbit
		self.orbit = [] # keeps track of all of the points that a Planet object has traveled along
		self.sun = False # tells us if planet is the sun, so it doesn't orbit
		self.distance_to_sun = 0 # value updates for every single planet so we can know its distances from the sun

		# planets x velocity and y velocity so they can circle around the Sun at a constant speed with it's distance from the Sun in meters
		self.x_vel = 0 
		self.y_vel = 0

	def draw(self, win):
		''' Draws the planet on the screen.

		args:
			win
				The window that the planet is gonna be drawn on.
		
		returns:
			Planet objects and their positions.	
		'''
		# centered and scaled x and y values of Planet object's distance from the sun in meters
		x = self.x * self.SCALE + WIDTH / 2 
		y = self.y * self.SCALE + HEIGHT / 2 

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2
				y = y * self.SCALE + HEIGHT / 2
				updated_points.append((x, y))

			pygame.draw.lines(win, self.color, False, updated_points, 2)

		pygame.draw.circle(win, self.color, (x, y), self.radius) # draws the Planet object on screen using the initialized values
		
		if not self.sun:
			distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE) 
			win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

	def attraction(self, other):
		''' Calculates the force of attraction between other objects using their distance and angles

		args:
			other
				Other Planet objects.

		returns:
			The gravitational force of x and y.
		'''
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x # takes the magnitude of the x value
		distance_y = other_y - self.y # takes the magnitude of the y value
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2) # the distance between the current object and the other object

		# checks if the object is the Sun, and assigns the distance to the Sun from an object to the distance value in the Planet class
		if other.sun:
			self.distance_to_sun = distance

		force = self.G * self.mass * other.mass / distance**2 # force of attraction using the mass of Planet objects and distance^2
		theta = math.atan2(distance_y, distance_x) # calculates the angle theta of other objects
		
		# calculates the x force and the y force
		force_x = math.cos(theta) * force 
		force_y = math.sin(theta) * force
		return force_x, force_y
	
	def update_position(self, planets): 
		''' Calculates the position of all the planets by calculating the force between the current planet and other planets,
			then calculate the velocity for the planets and move them by that velocity.

			args:

				planets:
					Takes in a list of planets
		
		'''
		total_fx = total_fy = 0 
		# sum all the forces together from all planets
		for planet in planets:
			if self == planet: 
				continue

			fx, fy = self.attraction(planet) # calculates the force exerted on Planet object
			total_fx += fx
			total_fy += fy

		# calculates the velocity of all the planets
		self.x_vel += total_fx / self.mass * self.TIMESTEP # F = m/a on the x plane
		self.y_vel += total_fy / self.mass * self.TIMESTEP # F = m/a on the y plane


		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))

def main():
	''' An infinite loop of the simulation until closed

	args:
		none

	returns:
		A window that keeps track of the different planets moving
	'''
	run = True
	clock = pygame.time.Clock() # initializes the frame rate of game

	sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30) 
	sun.sun = True # True, so the code doesn't draw the distance from the Sun using the Sun, and doesn't make the orbit for the Sun, which isn't needed

	# y_vel is so the planets dont go straight down the x-axis
	earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
	earth.y_vel = 29.783 * 1000 

	mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
	mars.y_vel = 24.077 * 1000

	mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
	mercury.y_vel = -47.4 * 1000

	venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
	venus.y_vel = -35.02 * 1000

	planets = [sun, earth, mars, mercury, venus] 

	while run:
		clock.tick(60) # maximum frame rate / updates per second 
		WIN.fill((0, 0, 0)) # RGB color that fills the entire screen (black in this case)

		for event in pygame.event.get(): # gets the different events that occur in pygame (if x button is pressed)
			if event.type == pygame.QUIT:
				run = False

		for planet in planets: 
			planet.update_position(planets) # updates the positions of planets till loop is broken
			planet.draw(WIN) # draws planets on our window

		pygame.display.update() # updates the display every loop

	pygame.quit()


main()
