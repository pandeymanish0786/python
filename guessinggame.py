import random
random_num=random.randint(1,10)
guess=None
while True:
	guess=input("pick a num between 1 to 10")
	guess=int(guess)
	if(guess<random_num):
		print("too low")
	elif(guess>random_num):
		print("too high")
	else:
		print("u won")
		play_again=input("do u want again?(y/n)")
		if(play_again=="y"):
			random_num=random.randint(1,10)
			guess=None
		else:
			print("thanku")
			break
