def swapPositions(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
List=[23,65,19,90]
pos1,pos2=1,3
print(swapPositions(List,pos1-1,pos2-1))




list1=[4,7,6,8,3,7,9,6,4]
list2=list(set(list1))
list2.sort() 
print("Smallest element is:",list2[0],list1)




list1=[4,7,6,8,3,7,9,6,4]
list2=list(set(list1))
list2.sort() 
print("largest element is:",list2[-1],list1)





list1=[4,7,6,8,3,7,9,6,4]
list2=list(set(list1))
list2.sort() 
print("Second largest element is:",list2[-2],list1)





start=int(input("Enter start of range:"))
end=int(input("Enter end of range:"))
for num in range(start,end+1):
    if num %2==0:
        print(num,end="")
        
        
        
def my_function(a):
    if(a%2==0):
        print("The number is even")
    else:
        print("The number is odd")
num=int(input("Enter the number:"))
my_function(num)




def my_function(country=" India "):
    print("I am going to"+country)
my_function(" Sewden ")
my_function(" Brazil ")
my_function()
my_function(" Dubai ")



def addnumbers (a,b):
    sum=a+b
    return sum
num1=int(input(""))
num2=int(input(""))
sum=addnumbers(num1,num2)
print("The sum is:",sum