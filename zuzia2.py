import math
import matplotlib.pyplot as plt
import numpy as np

def shm(omega_zero, gamma, t):
    a = 1
    if gamma > 2*omega_zero:            
        p = math.sqrt((gamma**2 / 4) - omega_zero**2)
        b = gamma / (2*p)
        x = (math.exp(-gamma*t / 2)) * (a*math.cosh(p*t) + b*math.sinh(p*t))
    elif gamma == 2*omega_zero:
        b = gamma / 2
        x = (math.exp(-gamma*t / 2)) * (a + b*t)
    else:
        w = math.sqrt(omega_zero**2 - (gamma**2 / 4))
        b = gamma / (2*w)
        x = (math.exp(-gamma*t / 2)) * (a*math.cos(w*t) + b*math.sin(w*t))
    return x

def main():
    gamma = float(input("Enter 'gamma' value: "))
    omega_zero = float(input("Enter 'omega_zero' value: "))
    points = int(input("Enter number of points: "))
    time = np.linspace(0, 5*math.pi / omega_zero, points)
    lists = []
    for t in time:
        x = shm(omega_zero, gamma, t)
        lists.append(x)
    plt.plot(time, lists, 'red')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Harmonic Oscillator')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.grid()
    plt.show()    

main()
