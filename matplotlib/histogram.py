import matplotlib.pyplot as plt
import numpy as np

#plot 1:(plotc)
x = np.array([0, 1, 2, 3])

plt.subplot(1, 2, 1)
plt.hist(x)

#plot 2:(scatter)
y = np.array([10, 20, 30, 40,50,60,70,80,90,100,110,120,130])

plt.subplot(1, 2, 2)

plt.hist( y)

plt.suptitle("MY SHOP")

plt.show()