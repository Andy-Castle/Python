# Loops break & continue

items = [1,2,3,4]

for item in items:
  if item == 2:
    continue #No imprime 2
  print(item)

for item in items:
  if item == 2:
    break #Solo imprime hasta el 1
  print(item)