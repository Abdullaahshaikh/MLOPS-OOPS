# Parent Class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object
d = Dog()
d.speak()   # inherited method
d.bark()