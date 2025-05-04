#Variable Scope

# age = 8 #Esta es un variable global

def test():
  age = 8 #Esto es una variable local
  print(age)

# print(age) #8
test() #()