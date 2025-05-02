import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice, "computer" : computer_choice}

  return choices

def checkWin(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock" and computer == "scissors":
    return "Rock smashes scissors! You win!"
  elif player == "rock" and computer == "paper":
    return "Paper covers rock! You lose."



print(checkWin("rock", "rock"))