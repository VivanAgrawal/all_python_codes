#Python program to show how to use assert keyword  
# defining a function  
def square_root( Number ):  
    assert ( Number < 0), "Give a positive integer"  
    return Number**(1/2)  
  
#Calling function and passing the values  
print( square_root( 36 ) )  
print( square_root( -36 ) )
