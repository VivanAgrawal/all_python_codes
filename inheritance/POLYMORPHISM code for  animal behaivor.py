   


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Polymorphic behavior
animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    print(animal.name + " says " + animal.make_sound())