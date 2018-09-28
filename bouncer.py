#ask for age
age=input("how old are u?")
if age:
	age=int(age)
	if age>=21:
		print("ypi r good to enter")
	elif age>=18:
		print("you can enter")
	else:
		print("you can not")
else:
	print("please enter an age")