import matplotlib.pyplot as plt
import numpy as np
#1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.title("SALES")
plt.subplot(2, 3, 1)
plt.plot(x,y)
#2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.title("SALES")
plt.subplot(2, 3, 2)
plt.plot(x,y)
#3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.title("SALES")
plt.subplot(2, 3, 3)
plt.plot(x,y)
#4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.title("SALES")
plt.subplot(2, 3, 4)
plt.plot(x,y)
#5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.title("SALES")
plt.subplot(2, 3, 5)
plt.plot(x,y)
#6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.title("SALES")
plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.suptitle("MY SHOP")

plt.show()