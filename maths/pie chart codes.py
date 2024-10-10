'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 



import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 



import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()''' 
 



import matplotlib.pyplot as plt
import numpy as np

y = np.array([12, 10, 8, 10])
mylabels = [" Sports", "Reading", "Gaming", "Other Activities"]

plt.pie(y, labels = mylabels,autopct='%1.1f%%')
plt.legend()
plt.show() 