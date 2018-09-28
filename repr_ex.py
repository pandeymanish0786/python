class human:
	def __init__(self,name="somebody"):
		self.name=name
	def __repr__(self):
		return self.name
dude=human()
print(dude)
manish=human(name="manish pandey")
print(f"{manish} is totally rad (probably)")
