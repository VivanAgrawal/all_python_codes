import matplotlib.pyplot as plt
import numpy as np

#plot 1:(plotc)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:(scatter)
x = np.array([0, 1, 2, 3,4,5,6,7,8,9,10,11,12])
y = np.array([10, 20, 30, 40,50,60,70,80,90,100,110,120,130])

plt.subplot(1, 2, 2)

colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, c=colors,cmap='viridis', s=sizes, alpha=0.5)

plt.suptitle("MY SHOP")

plt.show()