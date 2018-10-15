import math
import matplotlib.pyplot as plt
import numpy as np

omega_zero = 1
points = 200
time = np.linspace(0, 5*math.pi / omega_zero, points)
for t in time:
    print(t)