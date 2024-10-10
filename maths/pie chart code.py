# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:19:44 2023

@author: Admin
"""

import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [360,520,330,840,710,902]
marks = ['English', 'Maths', 'Physics', 'Chemistry', 'Eco', 'Accounts']

# Creating the pie chart
plt.pie(sizes, labels=marks)

# Showing the pie chart
plt.show()

import matplotlib.pyplot as plt