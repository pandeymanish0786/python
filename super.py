class animal:
	def __init__(self,name,species):
		self.name=name
		self.species=species
	def __repr__(self):
		return f"{self.name} is a {self.species}"
	def make_sound(self,sound):
		print(f"this animal says {sound}")
class cat(animal):
	def __init__(self,name,breed,toy):
		#self.name=name
		#self.species=species
		######animal.__init__(self,name,species)
		super().__init__(name,species="cat")
		self.breed=breed
		self.toy=toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")
blue=cat("blue","scootiosh fold","string")
blue.play()

