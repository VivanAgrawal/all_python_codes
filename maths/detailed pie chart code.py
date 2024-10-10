# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:21:56 2023

@author: Admin
"""

import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [30, 40, 20, 10]
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
colors = ['red','yellow',"blue","green"]
explode = (0, 0.1, 0, 0)

# Creating the pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%')

# Adding a title
plt.title('Favorite Fruits')

# Showing the pie chart
plt.show()