#  اسامة محمد صالح الهرش

import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['Rock', 'Paper', 'Scissors']
    
    print("Let's play Rock, Paper, Scissors!")
    print("Enter your choice (Rock, Paper, or Scissors):")
    player_choice = input().capitalize()
    
    while player_choice not in choices:
        print("Invalid choice. Please enter Rock, Paper, or Scissors:")
        player_choice = input().capitalize()
    
    computer_choice = random.choice(choices)
    
    print(f"You chose {player_choice}.")
    print(f"The computer chose {computer_choice}.")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

play_game()