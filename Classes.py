# Classes

class Animal:
  def walk(self):
    print("Walking...")

class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print("Woof!")

capuchina  = Dog("Capuchina", 2)

print(type(capuchina)) #<class '__main__.Dog'>

print(capuchina.name) #Capuchina
print(capuchina.age) #2

capuchina.bark() #Woof!

capuchina.walk() #Walking...