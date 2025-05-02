from enum import Enum

class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE.value) #1

print(State.INACTIVE.value) #0

print(State.ACTIVE.name) #ACTIVE

print(State.INACTIVE.name) #INACTIVE

#Esta es la unica manera de crear una constante en python

print(State["ACTIVE"].value) #1

print(list(State)) #[<State.INACTIVE: 0>, <State.ACTIVE: 1>]

print(len(State)) #2