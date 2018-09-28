class grumpydict(dict):
	def __repr__(self):
		print("none of your bussiness")
		return super().__repr__()
	def __missing__(self,key):
		print(f"u want {key}? ... well it aint here!")
	def __setitem__(self,key,value):
		print("u want to change the dictionary")
		print("ohk fine")
		super().__setitem__(key,value)
	def __contains__(self,item):
		print("no it aint in here")
		return False
data=grumpydict({"first":"tom","animal":"cat"})
print(data)
data["city"]="tokyo"
print(data)
y="city" in data
print(y)
