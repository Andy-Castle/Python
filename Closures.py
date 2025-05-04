# Closures
"""
Estas son funciones internas que recuerdan el estado de las variables
de su entorno, aunque el contexto externo ya haya terminado de ejecutarse
"""

def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1
    return count
  
  return increment

increment = counter()

print(increment()) #1
print(increment()) #2
print(increment()) #3
