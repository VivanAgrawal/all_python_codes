# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:34:59 2023

@author: Admin
"""

# get the number from the user
num = int(input("Enter a number: "))

# calculate the number of digits
num_of_digits = len(str(num))

# initialize the sum
sum = 0

# calculate the sum of the digits raised to the power of the number of digits
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_of_digits
    temp //= 10

# check if the number is an Armstrong number
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")