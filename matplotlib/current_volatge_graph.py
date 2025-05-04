import matplotlib.pyplot as plt
import numpy as np

current = np.array([0, 10,15])
voltage = np.array([10, 25,10])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("current and voltage graph" ,fontdict = font1)

plt.xlabel("current(A)", fontdict = font2)
plt.ylabel("voltage(V)", fontdict = font2)
plt.plot(current, voltage)

plt.suptitle("calculating resistance")
plt.show()