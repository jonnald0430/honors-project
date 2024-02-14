'''
notes:

these are equations to be somehow combined with our GUI
mass is in metres and takes user input
make sure grav constant and speed of light are in METRES

project uses metric system

'''

import numpy as np 
import scipy.constants as scipy
import matplotlib
import equations as eq


time_conversions_seconds = {

    'hour': 3600,
    'day': 86400,
    'month': 2.628e+6,
    'year': 3.154e+7,

}


EARTH_MASS = 5.9722*(10**24)
EARTH_RADIUS = 6378
G = scipy.gravitational_constant
C = scipy.speed_of_light

radius = []
while True:
    mass = input('Enter an integer for black hole mass: ')

    if mass.isdigit():
        mass = float(mass)
        radius = np.append(radius, eq.schwarzchild_radius(G, mass, C))
        print(f'Your radius is {radius[0]}')
        break
    else:
        print('Please enter a valid integer')

conversion_val = []
while True:
    seconds = input('Choose any number of seconds: ')

    if seconds.isdigit():
        seconds = int(seconds)
        break
    else:
        print('Please enter a valid integer')

while True:
    conversion = input('What calendrical unit would you like to convert into the amount of seconds you inputted? (hour, day, month, year): ')
    if conversion.lower() == 'hour' or conversion.upper() == 'HOUR':
        conversion_val = np.append(conversion_val, eq.conversion_seconds(seconds, 60, time_conversions_seconds['hour']))
        print(f'You would be at this position for: {conversion_val[0]} hour(s).')
        break
    elif conversion.lower() == 'day' or conversion.upper() == 'DAY':
        conversion_val = np.append(conversion_val, eq.conversion_seconds(seconds, 24, time_conversions_seconds['day']))
        print(f'You would be at this position for: {conversion_val[0]} day(s).')
        break
    elif conversion.lower() == 'month' or conversion.upper() == 'MONTH':
        conversion_val = np.append(conversion_val, eq.conversion_seconds(seconds, 30, time_conversions_seconds['month']))
        print(f'You would be at this position for: {conversion_val[0]} month(s).')
        break
    elif conversion.lower == 'year' or conversion.upper() == 'YEAR':
        conversion_val = np.append(conversion_val, eq.conversion_seconds(seconds, 365, time_conversions_seconds['year']))
        print(f'You would be at this position for: {conversion_val[0]} year(s).')
        break
    else:
        print('Invalid, try again')

distance_limit = radius[0]
while True:    
    black_hole_distance = int(input('Your distance from the black hole: '))
    if black_hole_distance > distance_limit:
        print('Placeholder')
        break
    else:
        black_hole_distance = print(f'You are in range of the Schwarzchild radius which means you (including light) cannot escape, thus we would not know what would happen enter a value greater than {distance_limit} meters: ')

