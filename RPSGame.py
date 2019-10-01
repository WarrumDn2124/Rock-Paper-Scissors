# Daniel Warrum
# Rock paper scissors Game-
#____________________________________________________________________________________
# Break into little pieces
# Welcome page, with name entry
# Score screen with computer, player(name), and ties.
# Options for game r, p ,s , q
# Game loop aquired until q is entered
# Each loop will get chosen by random (Choice)
# a coice from the player, compare the two, and update the score 
# When the game is over  when q is entered then it displays the score.

# WELCOME PAGE
# Prompt for the player name
# A welcome message

# _______________________________________________________________________________________________________________

# imports
import random
# Variables

playerScore = 0
computerScore = 0
ties = 0
# Make a list
cChoices =["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input ("Enter your name: ")

while True:
	print("Score: ")
	print("Computer: " + str(computerScore))
	print(name + ":" + str (playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for paper, 's' for Scissors and, 'q' to Quit: ")
	computerChoice = random.choice(cChoices)
	if choice == "q":
		break
	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r":
			print("Computer picked rock")
			print("This is a tie")
			ties = ties + 1 
	        

		elif computerChoice == "p":
			print("Computer picked paper")
			print("Paper beats rock")
			computerScore += 1 
			
		else:
			print("Computer picked scissors")
			print("Rock beats scissors")
			playerScore += 1 
	elif choice == "p":
		print(name + " Picked Paper")
		if computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1 
	        

		elif computerChoice == "r":
			print("Computer picked rock")
			print("Paper beats rock")
			playerScore += 1 
			
		else:
			print("Computer picked scissors")
			print("Scissors beat paper")
			computerScore += 1 
	elif choice == "s":
		print(name + " Picked scissors")
		if computerChoice == "r":
			print("Computer picked rock")
			print("Rock beats scissors")
			computerScore +=1 
	        

		elif computerChoice == "p":
			print("Computer picked paper")
			print("Scissors beats paper")
			playerScore += 1 
			
		else:
			print("Computer picked scissors")
			print("This is a tie")
			ties = ties + 1
	else:
		print("That is not an option!")