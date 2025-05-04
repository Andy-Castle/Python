# Recursion
#Es una funcion de python que se llama asi misma

# 3! = 3 * 2 * 1 = 6

def factorial(n):
  if n == 1: return 1
  return n * factorial(n-1)

print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120
