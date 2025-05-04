#Nested Functions

def talk(phrase):
  def say(word):
    print(word)
  
  words = phrase.split(" ")
  for word in words:
    say(word)

talk("I am going to buy the milk")

def count():
  count = 0 #Esta
  def increment():
    nonlocal count #Este nos permite acceder a la variable de arriba de count
    count = count + 1
    print(count)
  increment()

count()