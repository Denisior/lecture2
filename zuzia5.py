import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

def set_initial(v_initial, theta):
    #
    #
    return x, y, vx, vy

def acceleration(vx, vy, beta):
    #
    #
    return ax, ay

def step_forward(x, y, vx, vy, beta, delta_t):
    #
    #
    return x, y, vx, vy

def Fw(v, m, g, Fd):
    return (0, -m*g) - Fd

def main():
    delta_t = 0.001#float(input("Enter delta_t value: "))                    # Step interval in seconds
    v0 = 10#float(input("Enter v0 value: "))                              # Initial velocity [m/s]
    theta = math.radians(45)#float(input("Enter theta value: ")))   # Angle in degrees
    beta = 0.3#float(input("Enter beta value: "))                          # Drag coefficient
    g = const.g                                                 # Acceleration of gravity [m/s^2]
    m = 1                                                       # Mass [kg]
    p = 1.2                                                     # Air density [kg/m^3]
    A = math.pi*0.05
    t = np.arange(0, 10, delta_t)                               # Create an evenly spaced time-array
    a = np.zeros((int(1/delta_t), 2))
    v = np.zeros((int(1/delta_t), 2))
    pos = np.zeros((int(1/delta_t), 2))

    v[0] = (v0, v0)
    pos[0] = (0, 0)
    Fd = 0.5 * p * beta * A * v**2 * abs(v)*v

    for i in range(1000):
        a[i] = Fw(v[i], m, g, Fd) / m
        v[i+1] = v[i] + a[i]*delta_t
        pos[i+1] = pos[i] + v[i]*delta_t

    x = pos[:,0] 
    y = pos[:,1] 

    plt.plot(x,y)
    plt.show()


    
main()