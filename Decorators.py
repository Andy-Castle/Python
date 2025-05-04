# Decorators
"""
Un decorador es una funcion que toma otra funcion como argumento,
le agrega funcionalidad extra (antes o despues de ejecutarla) y
devuelve una nueva funcion. Sirve para modificar el comportamiento
de una funcion sin cambiar su codigo directamente
"""

def logtime(func):
  def wrapper():
    # do something before
    print("before")
    val = func()
    # do something after
    print("after")
    return val
  return wrapper

@logtime
def hello():
  print("Hello")


hello() #before
        #Hello
        #after