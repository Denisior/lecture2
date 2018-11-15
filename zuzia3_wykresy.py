import math
import matplotlib.pyplot as plt
import numpy as np

def logpower(voltage, current):
    p = math.log(voltage*current)
    return p
    
def main():
    filename = input("File name to open: ")
    filein = open(filename, "r")
    f = 25000
    t = 1 / f
    power_data = []
    time_data = []
    temp = 0
    voltage = []
    current = []
    multiply_vxi = []
        
    for line in filein.readlines():
        if not line.startswith("#"):
            tokens = line.split(",")
            voltage.append(float(tokens[0]))
            current.append(float(tokens[1]))
            voltage_data = float(tokens[0])
            current_data = float(tokens[1])
            multiply_vxi.append(voltage_data*current_data)
            power_data.append(logpower(voltage_data, current_data))
            temp += t
            time_data.append(temp)
    filein.close()
    plt.plot(time_data, power_data, time_data, voltage, time_data, current, time_data, multiply_vxi)
    plt.grid()
    plt.title("Circuit at a rate of 25kHz")
    plt.xlabel("Time [s]")
    plt.ylabel("ln(Power) [W]")
    plt.legend(('p(t)', 'v(t)', 'i(t)', 'v(t)*i(t)'))
    plt.show()

main()