# Modules

#import Dog #Esto importado todo el archivo

#from Dog import bark #Este solo importa lo que se necesita

# Dog.bark()

#from lib import dog #Esto importado todo el archivo cuando esta en la carpeta lib

# Dog.bark()

from lib.Dog import bark #Esta es una forma de importar solo la funcion cuando esta en una carpeta lib

bark()

"""
math for math utilities
re for regular expressions
json to work with JSON
datetime to work with dates
sqlite3 to use SQLite
os for Operating System utilities
random for random number generation
statistics for statistics utilities
requests to perform HTTTP network requests
http to create HTTP servers
urllib to manage URLs
"""

#import math
from math import sqrt

print(sqrt(4))
