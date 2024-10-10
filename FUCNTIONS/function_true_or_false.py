# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:39:28 2023

@author: Admin
"""

def evennumber(a):
    sum=a%2==0
    return sum 
    
num1=int(input("Enter a number:"))
sum=evennumber(num1)
print("The  number is even:",sum)

def oddnumber(a):
    sum=a%2!=0
    return sum 
    
num1=int(input("Enter a number:"))
sum=evennumber(num1)
print("The  number is odd:",sum)