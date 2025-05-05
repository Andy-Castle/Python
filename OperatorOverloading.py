# Operator Overloading

"""
El operator overloading significa que puedes personalizar el comportamiento
de los operadores (+ , -, >, etc) cuando se usan con objetos de tus
propias clases
"""


class Dog:
  # the dog class
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __gt__(self, other):
    return True if self.age > other.age else False


roger = Dog("Roger", 8)
syd = Dog("Syd", 9)

print(roger > syd)

"""
__add__() respond to the + operator
__sub__() respond to the - operator
__mul__() respond to the * operator
__truediv__() respond to the / operator
__floordiv() respond to the // operator
__mod__() respond to the % operator
__pow__() respond to the ** operator
__rshift__() respond to the >> operator
__and__() respond to the & operator
__or__() respond to the | operator
__xor__() respond to the ^ operator
"""

