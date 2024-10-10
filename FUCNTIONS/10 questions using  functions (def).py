# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:27:30 2023

@author: Admin
"""

#Code1
def my_function():
  print("Hello from a function")

my_function()


#Code2
def my_function(fname):
  print(fname + " Hand")

my_function("Right")
my_function("Left")


#Code3
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


#Code4
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#Code5
def myfunction():
  pass


#Code6
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
 

#Code7
def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


#Code8
def is_prime(n):
	if n in [2, 3]:
		return True
	if (n == 1) or (n % 2 == 0):
		return False
	r = 3
	while r * r <= n:
		if n % r == 0:
			return False
		r += 2
	return True
print(is_prime(78), is_prime(79))


#Code9
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)


#Code10
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)









