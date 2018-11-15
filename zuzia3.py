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
        
    for line in filein.readlines():
        if not line.startswith("#"):
            tokens = line.split(",")
            voltage_data = float(tokens[0])
            current_data = float(tokens[1])
            power_data.append(logpower(voltage_data, current_data))
            temp += t
            time_data.append(temp)
    filein.close()
    plt.plot(time_data, power_data)
    plt.grid()
    plt.title("Circuit rate of 25kHz")
    plt.xlabel("Time [s]")
    plt.ylabel("ln(Power) [W]")
    plt.legend(('p(t)', ''))
    plt.show()

main()