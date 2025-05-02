print("Andy".upper()) #ANDY
print("AnDy".lower()) # andy
print("andy person".title()) # Andy Person
print("andy person".islower()) #True

#isalpha() to check if a string contains only characters and is not empty
print("Hola".isalpha())     # True
print("Hola123".isalpha())  # False
print("".isalpha())         # False

#isalnum() to check if a string contains characters or digits and is not empty
print("Hola123".isalnum())  # True
print("Hola!".isalnum())    # False
print("".isalnum())         # False

#isdecimal() to check if a string contains digits and is not empty
print("12345".isdecimal())  # True
print("123a".isdecimal())   # False
print("".isdecimal())       # False

#lower() to get a lowercase version of a string
print("HeLLo".lower())  # 'hello'

#islower() to check if a string is lowercase
print("mundo".islower())  # True
print("Mundo".islower())  # False

#upper() to get anf uppercase version of a string
print("hola".upper())  # 'HOLA'

#isupper() to check if a string is uppercase
print("HOLA".isupper())  # True
print("Hola".isupper())  # False

#tittle() to get a capitalized version of a string
print("bienvenido a python".title())  # 'Bienvenido A Python'

#startswith() to check if the string starts with a specific substring
print("pythonista".startswith("py"))  # True
print("pythonista".startswith("java"))  # False

#endswith() to check if the string ends with a specific substring
print("documento.pdf".endswith(".pdf"))  # True
print("documento.pdf".endswith(".txt"))  # False

#replace() to replace a part of a string
print("Me gusta Python".replace("Python", "JavaScript"))  
# 'Me gusta JavaScript'

#split() to split a string on a specific character separator
print("uno,dos,tres".split(","))  
# ['uno', 'dos', 'tres']

#strip() to trim the whitespace from a string
print("  hola mundo  ".strip())  
# 'hola mundo'

#join() to append new letters to a string
letras = ["H", "o", "l", "a"]
print("".join(letras))  # 'Hola'

#find() to find the position of a substring
print("programador".find("grama"))  # 3
print("programador".find("z"))      # -1

####
name = "Andy"
print(name.lower())
print(len(name)) #4
print("dy" in name) # 'in' checa si "Andy" contiene "dy" 