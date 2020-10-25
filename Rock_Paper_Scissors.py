import random

def game():
	while True:
		choices = ['rock', 'paper', 'scissors']
		user_choice = input("Rock, Paper, or Scissors?: ").lower()
		bot_choice = random.choice(choices)

		if user_choice == bot_choice:
			print("Tie! Onto the next round! \n")

		elif user_choice == "rock" and bot_choice == "scissors":
			print("The bot has chosen scissors! You win! \n")

		elif user_choice == "scissors" and bot_choice == "rock":
			print("The bot has chosen rock! You lose! :( \n")

		elif user_choice == "paper" and bot_choice == "rock":
			print("The bot has chosen rock! You win! \n")

		elif user_choice == "rock" and bot_choice == "paper":
			print("The bot has chosen paper! You lose! :( \n")

		elif user_choice == "scissors" and bot_choice == "paper":
			print("The bot has chosen paper! You win! \n")

		elif user_choice == "paper" and bot_choice == "scissors":
			print("The bot has chosen scissors! You lose! :( \n")
			
		else: 
			print("You have not chosen rock, paper, or scissors, please retry. \n")
			game()

game()
