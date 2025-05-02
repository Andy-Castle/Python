done = False
# done = False
#done = -1 #true
#done = "" #false

print(type(done) == bool)

if done:
  print("Yes")
else:
  print("No")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])

print(read_any_book) #retorna true si cualquiera de esos es true

ingredients_purchased = True
meal_cooked = False
ready_to_Serve = all([ingredients_purchased, meal_cooked]) #retorna true si todos los valores son true

print(ready_to_Serve)