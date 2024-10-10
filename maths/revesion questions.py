
'''#using market 
numbers=[2,4,23,34,21]
maxi=max(numbers)
mini=min(numbers)
print("miximum in list:",maxi)
print("minimum in list",mini)

# adding and deleting elements in touple(python)
#adding
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

#deleting
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)'''

#declering a dictonary
dic={"a":"apple","b":"ball","c":"cat"}
print(dic)
se=input("Enter the key which you want to print")
print(dic[se])


















































