class pet:
	allowed=["cat","dog","fish","rat"]
	def __init__(self,name,species):
		if species not in pet.allowed:
			raise ValueError(f"u can't have,{species} pet!!!!")
			self.name=name
			self.species=species
	def set_species(self,species):
		if species not in pet.allowed:
			raise ValueError(f"you can't have a {species} pet!")
			self.species=species
cat=pet("blue","elephant")
dog=pet("wyatt","dog")
