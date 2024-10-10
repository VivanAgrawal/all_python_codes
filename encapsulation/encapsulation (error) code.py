
class MyClass:
    def __init__(self):
        self.__private_var = 10

    def display(self):
        print(self.__private_var)


obj = MyClass()
obj.display()  # Output: 10
print(obj.__private_var)