import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 10, 20, 30, 40, 50])  # Time 
distance = np.array([0, 10, 20, 30, 40, 50])  #distance

plt.plot(time,distance, marker='o')
plt.title('Distance-Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Distance(km)')
plt.grid(True)
plt.show()

obj_name=str(input("Enter the object:"))
d=int(input("Enter distance:"))
t=int(input("Enter time:"))

v=d/t

print(f"The speed of {obj_name} is",v)


