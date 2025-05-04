# map(), filter(), reduce()

#MAP
numbers = [1,2,3]

# def double(a):
#   return a * 2

# double = lambda a : a* 2

# result = map(double, numbers)
result = map( lambda a : a* 2, numbers)

print(list(result)) #[2, 4, 6]


#FILTER

# isEven = lambda n : n % 2 == 0

def isEven(n):
  return n % 2 == 0

result2 = filter(isEven, numbers)

print(list(result2)) #[2]


#REDUCE

from functools import reduce

expenses = [("Dinner", 80), ("Car repair", 120)]

# sum = 0

# for expense in expenses:
#   sum += expense[1]

sum = reduce(lambda a,b: a[1] + b[1], expenses)

print(sum) # 200