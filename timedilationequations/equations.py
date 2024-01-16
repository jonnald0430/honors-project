'''
equations used to calculate distance 
and things of that nature
'''
import numpy as np

def schwarzchild_radius(gravitational_constant, mass ,speed_of_light):
    #calculates the radius the users input needs to be in 
    return (2* float(gravitational_constant) * float(mass) / float(speed_of_light**2)) 

def conversion_seconds(seconds, time_int, time_conv):
    #calculates conversions (in seconds)
    return seconds * (time_int/time_conv)

def time_dilation(mass, radius):
    # calculates time dilation compared to a normal time
    return np.sqrt(1 - ((2*G*mass)/radius*C**2))

