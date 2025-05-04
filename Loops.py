# Loops

condition = True
while condition == True:
  print("The condition is True")
  condition = False

count = 0
while count < 4:
  print("The condiution is True")
  count += 1

print("After the loop")

items = [1,2,3,4]
for item in items:
  print(item)

# for item in range(15):
#   print(item)

items = ["Andy","Frida","Pamela","Yessenia"]
for index, item in enumerate(items):
  print(index,item)

