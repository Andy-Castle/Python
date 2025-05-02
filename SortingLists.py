items = ["Andy", "Frida", "Pepe", "ana", "Zyon", "Juan"]

# items.sort() #ordena la lista de forma ascendente
# print(items) #ordena las capitales primero y las minusculas despues


# itemscopy = items[:]
# print(itemscopy)

# items.sort(key=str.lower) #ordena la lista de forma ascendente, pero con el key no importa la regla de las mayusculas
# print(items) 

print(sorted(items, key=str.lower)) #Este crea una nueva lista sin modificar la original

print(items)
