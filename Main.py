"""
Author: Tyler Provencher tyler@provenchermultimedia.com

This is a simple command line Rock, Paper, Scissors game vs the Computer. First to win 4 games wins. 
The computers choice is randomized using the random library. 
"""

import random

def get_user_choice():
  """Gets the user's choice of rock, paper, or scissors."""
  while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice in ["rock", "paper", "scissors"]:
      return choice

def get_computer_choice():
  """Gets the computer's choice of rock, paper, or scissors."""
  return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
  """Determine the winner of a round of rock paper scissors."""
  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "user"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "user"
  elif user_choice == "paper" and computer_choice == "rock":
    return "user"
  else:
    return "computer"

def play_game():
  """Plays a game of rock paper scissors."""
  user_score = 0
  computer_score = 0
  print("Welcome to Tpro's Rock, Paper, Scissors Game! This is a best of 7 vs the Computer. Good Luck!")

  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
      user_score += 1
    elif winner == "computer":
      computer_score += 1

    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    if winner == "user":
      print("You win!")
    elif winner == "computer":
      print("Computer wins!")
    elif winner == "tie":
      print("Tie!")
      
    #Display current score
    print(f"Current Score:\n User: {user_score}, Computer: {computer_score}")

    if user_score == 4 or computer_score == 4:
      break

  print(f"Final score: User {user_score}, Computer {computer_score}")

if __name__ == "__main__":
  play_game()