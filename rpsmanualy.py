#rock paper scissors game for two person
print("rock....")
print("paper....")
print("scissors....")
player1=input(" player 1,make your move:  ")
player2=input("player2, make your mmove:  ")
if player1 == "rock" and player2=="scissos":
	print("player 1,,you win ..")
elif  player1 == "rock" and player2=="paper":
	print("player 2... u win....")
elif player1==player2:
	print("its a tie")
else:
	print("something went wrong")
