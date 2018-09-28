class aquatic:
	def __init__(self,name):
		print("aquate init!!")
		self.name=name
	def swim(self):
		return f"{self.name} is swiming"
	def greet(self):
		return f"i am {self.name} of the sea!!!"
class ambulatory:
	def __init__(self,name):
		print("ambulatory init!!")
	def walk(self):
		return f"{self.name} is walking"
	def greet(self):
		return f"i am {self.name} of the land"
class penguin(ambulatory,aquatic):
	def __init__(self,name):
		print("penguin init")
		ambulatory.__init__(self,name=name)
		aquatic.__init__(self,name=name)
jaws=aquatic("jaws")
lassie=ambulatory("lassie")
captain_cook=penguin("captain cook")
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())
print(f"swim is inheritance of penguin: {instance(captain_cook,penguin)}")
