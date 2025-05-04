# Sets
"""
Los sets no permiten duplicados, no tienen orden,
son utiles para operaciones matematicas como interseccion,
unión, diferencia, etc
"""
set1 = {"Roger", "Syd", "Roger"} #Si hay un roger abajo como este caso, no se duplicara
set2 = {"Roger"} #Este en intersect tenia "Roger"

intersect = set1 & set2 #Esto Interseccion
"""
Este & devuelve los elementos que estan en ambos sets
"""
print(intersect) # {'Roger'}

mod = set1 | set2 #Este en set2 tenia "Luna"
"""
Este | devuekve todos los elementos de ambos sets, sin repetir
"""
print(mod) # {'Syd', 'Luna', 'Roger'}

mod = set1 - set2 #
"""
Este - devuelve los elementos que estan en set1 pero no en set2
"""
print(mod) # {'Syd'}

mod = set1 > set2 #
"""
Este devuelve True si set1 contiene todos los elementos de set2, osea, si
set1 es un superconjunto de set2
"""
print(mod) # True


mod = set1 < set2 #
"""
Este devuelve True si todos los elementos de set1 están en set2, es decir,
si set1 es un subconjunto.
"""
print(mod) # False

print(list(set1)) #['Syd', 'Roger']