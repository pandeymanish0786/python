def make_song(verses=99,beverage="soda"):
	for num in range(verses,-1,-1):
		if num>1:
			yield"{num} bottle of {beverage} is left"
		elif num==1:
			yield"only 1 bottle of{beverage} left!"
		else:
			yield"no more {beverage}!!!!"
