import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 10, 20, 30, 40, 50])  # Time 
velocity = np.array([0, 20, 20, 20, 20, 20])  #velocity

plt.plot(time, velocity, marker='o')
plt.title('Velocity-Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.show()


