# Functions

# def hello(name, age):
#   print("Hello " + name + ", you are " + str(age) + " years old")

# hello("Andy", 25)

# def change(value):
#   value["name"] = "Isaac"

# val = {"name": "Andy"} #los dictionaries si se pueden porque son mutables
# change(val)

# print(val)

# def hello(name):
#   print("Hello " + name + "!")
#   return name

# print(hello("Andy"))

def hello(name):
  if not name:
    return
  print("Hello " + name + "!")

hello("Andy")