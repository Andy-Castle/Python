#Dictionaries

dog = {"name" : "Capuchina", "age" : 2, "color": "white"}

print(dog["name"]) #Capuchina

dog["name"] = "Maki"
print(dog["name"]) #Maki

print(dog.get("name")) #Maki

print(dog.get("color", "brown")) #si no hay colo devolvera "brown"

print(dog.pop("name")) #Elimina el "name"
print(dog)


dog.popitem() #Elimina y devuelve el ultimo par de clave-valor insertado en el diccionario

print(dog)

print("color" in dog) #False

print(dog.keys()) #dict_keys(['age'])

print(list(dog.keys())) #['age']

print(dog.values()) #dict_values([2])

print(list(dog.values())) #[2]

print(list(dog.items())) #[('age', 2)]

print(len(dog)) #1

dog["favorite food"] =  "Meat" #Esto es una forma de añadir un clave-valor
dog["color"] =  "Brown"
print(dog)

del dog['color'] #Este elimina el color
print(dog)

dogCopy = dog.copy() #Esto es para copiar el dcitionary





