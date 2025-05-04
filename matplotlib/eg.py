import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 10,15])
ypoints = np.array([10, 25,10])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data" ,fontdict = font1)

plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(y1,y2)
plt.plot(xpoints, ypoints, 'o:r', ms = 20,mfc = 'g',mec='b',linestyle = 'dotted',color = 'b',linewidth = '20.5')

plt.grid(color = 'r', linestyle = '--', linewidth = 5)

plt.suptitle("MY SHOP")
plt.show()