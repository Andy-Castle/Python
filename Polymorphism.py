# Polymorphism
"""
Polimorfismo significa muchas formas, se refiere a que diferentes
clases pueden tener metodos con el mismo nobre, pero con
comportamientos distintos
"""


class Dog:
  def eat(self):
    print("Eating dog food")

class Cat:
  def eat(self):
    print("Eating cat food")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()