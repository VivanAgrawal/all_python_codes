#Code1
# function for subtraction of 2 numbers.
def subNumbers(x, y):
    return (x-y)
 
# main code
a = 90
b = 50
 
# finding subtraction
result = subNumbers(a, b)
 
# print statement
print("subtraction of ", a, " and ", b, " is = ", result)



#Code2
# A function name prime is defined
# using def
def prime(n):
    x = 1
    count = 0
    while count < n:
        for d in range(2, x, 1):
            if x % d == 0:
                x += 1
        else:
            print(x)
            x += 1
            count += 1
 
# Driver Code
n = 10
 
# print statement
print("First 10 prime numbers are:  ")
prime(n)




#code3
# Function name factorial is defined
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
 
# Main code
num = 6
 
# check is the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))
    
    
    
    
    
    
#Code4
# Define function to calculate cube root
# using def keyword
  
def calculate_cube_root(x):
    return x**(1/3)
  
# Call the def function to calculate cube
# root and print it
print(calculate_cube_root(27))
  
# Define function to check if language is present in
# language list using def keyword
languages = ['Sanskrut', 'English', 'French', 'German']
  
def check_language(x):
    if x in languages:
        return True
    return False
  
# Call the def function to check if keyword 'English'
# is present in the languages list and print it
print(check_language('English'))





#Code5
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist





#Code6
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist





#Code7
def findPerSqr(x):
    return 4*x

print("Enter the Side Length: ", end="")
s = float(input())

p = findPerSqr(s)
print("\nPerimeter of square= {:.2f}".format(p))





#Code8
def findPeri(a, b):
    p = 2*(a+b)
    return p

print("Enter Length and Breadth of Rectangle: ", end="")
l = float(input())
b = float(input())

res = findPeri(l, b)
print("\nPerimeter of rectangle= {:.2f}".format(res))





#Code9
import math  
  
def area_of_the_circle (Radius):   
    area = Radius** 2 * 3.14
    return area  
  
Radius = float (input ("Please enter the radius of the given circle: "))  
print (" The area of the given circle is: ", area_of_the_circle (Radius))  






#code10
def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * 3.14 * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)

print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)

    
    
    
    
    
