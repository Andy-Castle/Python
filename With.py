# Exceptions with

"""
El bloque with en python se usa para manejar recursos como archivos de
forma mas segura y limpia, especialmente cuando esos recursos necesitan
cerrarse despues de usarlos
"""

filename = '/Users/Andy/test.txt'

# try:
#   file = open(filename, 'r')
#   content = file.read()
#   print(content)
# finally:
#   file.close()

with open(filename, "r") as file:
  content = file.read()
  print(content)