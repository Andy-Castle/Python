# List Compressions

"""
La list comprehension es una forma concisa y elegante crear listas
a partir de una secuencia, aplicando una operacion a cada elemento.
"""

numbers = [1,2,3,4,5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

# numbers_power_2 = []
# for n in numbers:
#   numbers_power_2.append(n**2)

# numbers_power_2 = list(map(lambda n : n**2, numbers))