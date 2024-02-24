'''
equations used to calculate distance 
and things of that nature
'''

import numpy as np


# these are used for the gui and user input
def schwarzchild_radius(gravitational_constant, mass ,speed_of_light):
    #calculates the radius the users input needs to be in 
    return (2* float(gravitational_constant) * float(mass) / float(speed_of_light**2)) 

def conversion_seconds(seconds, time_int, time_conv):
    #calculates conversions (in seconds)
    return seconds * (time_int/time_conv)

def time_dilation(gravitational_constant, mass, radius, speed_of_light):
    # calculates time dilation compared to a normal time
    return np.sqrt(1 - ((2*gravitational_constant*mass)/radius*speed_of_light**2))

