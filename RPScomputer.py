#rock paper scissors game for computer and one person
from random import randint
print("rock....")
print("paper....")
print("scissors....")
player=input(" player 1,make your move:  ").lower()

rand_num=randint(0,2)
if rand_num==0:
	computer="rock"
elif rand_num==1:
	computer="paper"
else:
	computer="scissors"
print(f"computer playes{computer}")
if player==computer:
	print("draw")
elif player=="rock":
	if computer=="scissors":
		print("player wins")
	else:
		print("computer win")
elif player=="paper":
	if computer=="rock":
		print("player wins")
	else:
		print("computer win")
elif player=="scissors":
	if computer=="paper":
		print("player wins")
	else:
		print("computer win")
elif player=="rock":
	if computer=="scissors":
		print("player wins")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")