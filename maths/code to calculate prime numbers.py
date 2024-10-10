# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 10:15:52 2023

@author: Admin
"""
#user defined range
user_range_start=int(input("Enter the start range to find prime numbers:"))
user_range_end=int(input("Enter the end range to find prime numbers:"))

#for loop

for num in range(user_range_start,user_range_end+1):
    if num>1:
        for i in range (2,num):
            if(num%i==0):
                break
        else:
                print(num)
        










