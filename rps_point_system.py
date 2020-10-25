import random

score = 10

def intro():
	print("""Welcome to the game of Rock, Paper, Scissors!! In this game, you will only have 10 rounds to play. 
You start off with 10 points.
Everytime you win a round, you gain a point. 
However, if you lose a round, then you lose a point. 
The goal of this game is to have 15 points by the end of the game. 
If you end up meeting this goal, then you win! If not, then you can always retry. Good Luck!\n""")
	game(score)

def game(score):
	count = 0
	while count < 10:
		choices = ['rock', 'paper', 'scissors']
		user_choice = input("Rock, Paper, or Scissors?: ").lower()
		bot_choice = random.choice(choices)
		print(bot_choice)

		if user_choice == bot_choice:
			print("Tie! Onto the next round! \n")
			count += 1

		elif user_choice == "rock" and bot_choice == "scissors":
			print("The bot has chosen scissors! You win! \n")
			score += 1 
			count += 1

		elif user_choice == "scissors" and bot_choice == "rock":
			print("The bot has chosen rock! You lose! :( \n")
			score -= 1
			count += 1

		elif user_choice == "paper" and bot_choice == "rock":
			print("The bot has chosen rock! You win! \n")
			score += 1
			count += 1

		elif user_choice == "rock" and bot_choice == "paper":
			print("The bot has chosen paper! You lose! :( \n")
			score -= 1
			count += 1

		elif user_choice == "scissors" and bot_choice == "paper":
			print("The bot has chosen paper! You win! \n")
			score += 1
			count += 1

		elif user_choice == "paper" and bot_choice == "scissors":
			print("The bot has chosen scissors! You lose! :( \n")
			score -= 1
			count += 1

		else: 
			print("You have not chosen rock, paper, or scissors, please retry. \n")

		if count == 10:
			ending(score)

def ending(score):
	print(f"""\nYou have reached the end!
Your total points: {score} points.""")
	if score >= 15:
		print("Congrats! You have successfully earned 15 points! You win!!! :) \n")
	else:
		print("Sadly, have have not earned 15 points. You lose. :( \n")

	question = input("If you would like to play again, and possibly try to gain a higher amount of points, type 'Y' and press enter. If not, type 'N'. and press enter: ").lower()
	if question == "y":
		intro()
	elif question == "n":
		print("Thank you for playing! Hopefully you enjoyed it!")

intro()