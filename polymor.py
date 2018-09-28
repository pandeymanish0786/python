class animal:
	def speak(self):
		raise NotImplementedError("subclass needs to implemed")
class dog(animal):
	def speak(self):
		return"woof"
class cat(animal):
	def speak(self):
		return "meow"
class fish(animal):
	pass
d=dog()
print(d.speak())
f=fish()
print(f.speak())
