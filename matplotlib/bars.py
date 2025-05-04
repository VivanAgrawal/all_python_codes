import matplotlib.pyplot as plt
import numpy as np



x = np.array(['maths', 'science', 'english','sst','hindi','marathi'])
y = np.array([10,50,30,40,20,60])

plt.subplot(1, 2, 1)
plt.xlabel('subjects')
plt.ylabel('marks')
plt.bar(x, y)
plt.title('student 1')
plt.suptitle("students marks")


x = np.array(['maths', 'science', 'english','sst','hindi','marathi'])
y = np.array([60,50,40,40,60,90])

plt.subplot(1, 2, 2)
plt.xlabel('subjects')
plt.ylabel('marks')
plt.bar(x, y)
plt.title('student 2')

plt.show()