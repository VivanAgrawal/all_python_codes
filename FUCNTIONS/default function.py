

def my_function(country="India"):
    print("I am from:"+country)
my_function("Sewden")
my_function("Brazil")
my_function()
my_function("every where")






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