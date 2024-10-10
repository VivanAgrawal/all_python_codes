class Person:
    def __init__(self, name):
        self.name = name

person = Person("Bob")

try:
    print(person.age)  # This will raise an AttributeError
except AttributeError:
    print("Error: 'age' attribute not found")