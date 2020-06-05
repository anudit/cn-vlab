import numpy as np
import matplotlib.pyplot as plt

def plot(bindata, repeatFactor=100):

    pltdata = []
    locs = [x*repeatFactor for x in range(len(bindata))]
    ticks = [x for x in range(len(bindata))]

    for ind, val in enumerate(bindata):
        pltdata += [val]*repeatFactor

    plt.xticks(locs, ticks)
    plt.plot(pltdata)
    return plt

bindata = [1, -1, 0 , 1, 0, 0, 1, -1]
plt = plot(bindata)
plt.show()


bindata = [0, 0,1,0,1,1,1,0,1,1,-1,-1,1,1,0,-1,0]
plt = plot(bindata)
plt.show()
