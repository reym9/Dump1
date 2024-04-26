import time
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

fig, ax = plt.subplots()

x=np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)

line,=ax.plot(x,y)


for delay in np.arange(0, np.pi, 0.1):
    #faza increase i dohodit do pi
    y=np.cos(x+delay)

    line.set_ydata(y)

    #plt.clf() - polnoe cleaning

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)

plt.ioff()
plt.show()