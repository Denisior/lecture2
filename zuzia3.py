import math
import matplotlib.pyplot as plt
import numpy as np

def logpower(voltage, current):
    p = math.log(voltage*current)
    return p
    
def main():
    filename = input("File name to open: ")
    filein = open(filename, "r")
    power_data = []
    f = 25000
    t = 1 / f
    filelines = filein.readlines()
    time_data = np.arange(0, len(filelines) * t, t)
    #print(time_data)
    for line in filelines:
        tokens = line.split(",")
        print(tokens)
        voltage_data = float(tokens[0])
        current_data = float(tokens[1])
        power_data.append(logpower(voltage_data, current_data))
    #print(power)
    filein.close()
    plt.plot(time_data, power_data)       
    plt.show()

main()