dogs = ["Luna", False, 2, "Capuchina", 1, True, "Diva", 8]

print("Luna" in dogs) #True
print("Diva" in dogs) #False

print(dogs[0]) #Luna
print(dogs[2]) #2

dogs[2] = "Queen"
print(dogs)

print(dogs[-1]) #8

print(dogs[2:4]) #['Queen', 'Capuchina']

print(dogs[:3]) #['Luna', False, 'Queen']

print(len(dogs)) #8

dogs.append("Alberto") #Este sirve para añadir en una lista
print(dogs)

dogs.extend(["Jaime", 5]) #Extiende la lista y permite agregar mas de uno
print(dogs)

dogs += ["Mauro", 10] #Hace lo mismo que extends
print(dogs)

dogs += "Pepe" #sin los corchetes este añade letra por letra
print(dogs)

dogs.remove("Alberto") #Elimina este de la lista
print(dogs)

print(dogs.pop()) #remueve el ultimo elemento de la lista
print(dogs)


items = ["Luna", False, 2, True, "Diva", 8]

items.insert(2, "Test") #En el index 2 despues de este añadio el Test
print(items)

items[1:1] = ["Test1", "Test2"] #En el index 1 despues de este añadio estos
print(items)
