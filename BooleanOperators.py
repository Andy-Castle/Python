condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

##Esto retorna el segundo valor si el primero es Falsy
print(0 or 1) ##1
print(False or 'hey') ##'hey'
print('hi' or 'hey') ##'hi'
print([] or False) ##'False'
print(False or []) ##'[]'

##Si el primero es false, devuelve ese operador
print(0 and 1) ##0
print(1 and 0) ##0
print(False and 'hey') ##False
print('hi' and 'hey') ##'hey'
print([] and False) ##[]
print(False and []) ##False
