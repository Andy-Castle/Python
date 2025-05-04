# Tuples
#Son como las listas pero son inmutables
#No puedes añadir o eliminar

names = ("Roger", "Syd", "Beau")

print(names[0]) #Roger
print(names.index("Roger")) #0

print(names[-1]) #Syd

print(len(names)) #2

print("Roger" in names) #True

print(names[0:2]) #('Roger', 'Syd')

print(sorted(names)) #['Beau', 'Roger', 'Syd']

newTuple = names + ("Andy", "Frida")
print(newTuple)

