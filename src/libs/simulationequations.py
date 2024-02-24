import scipy 
import numpy
from scipy.integrate import quad
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def radial_potential(r,b):
    return r**4 - b**2*r**2 + 2 *b**2*r

def minrs(b):
    temp = np.cbrt(b**2)*((-1 + np.sqrt(1+0j-b**2/27))**(1/3)+(-1 - np.sqrt(1+0j-b**2/27))**(1/3))
    return np.real(temp). real if np.imag(temp) < 1e-10 else 0

def d_phi_dr(r,b):
    return b / np.sqrt(radial_potential(r,b))

def d_phi_dx(x,b,rt):
    return -2*b*np.abs(x) / \
    (
        (x**2+rt) * np.sqrt(-((b**2*(-2+x**2+rt)) / (x**2+rt)) + (x**2+rt)**2)
    )

def phi(xi,b):
    rt = minrs(b)
    if xi.imag != 0:
        return np.inf
    if rt == 0 and xi < 0:
        return quad(d_phi_dx, np.inf, 0, args=(b,rt))
    return quad(d_phi_dx, np.inf, xi, args=(b,rt))

def generate_trajectory(ximin, ximax, b, steps):
    rt = minrs(b)
    coordinates = np.ndarray([steps, 2])
    for step in range(steps):
        xi = step*(ximax - ximin)/steps + ximin
        rs = 0 if rt == 0 and xi < 0 else (xi**2 + rt)
        coordinates[step][0]= rs
        coordinates[step][1] = phi(xi, b)[0]
    x_values = list(map(lambda x: x[0]*numpy.cos(x[1]),coordinates))
    y_values = list(map(lambda x: x[0]*numpy.sin(x[1]),coordinates))
    return x_values, y_values