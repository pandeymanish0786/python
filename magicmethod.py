class human:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
	def __repr__(self):
		return f"human named {self.first} {self.last} aged {self.age}"
	def __len__(self):
		return self.age
	def __add__(self,other):
		if isinstance(other,human):
			return human(first="newborn" ,last=self.last ,age=0)
		return "you can't add that!!"
	def __mul__(self,other):
		if isinstance(other,int):
			return[self for i in range(other)]
		return "can't multiply"
j=human("jenny","larsen",47)
k=human("kevin","jones",49)
print(j)
print(len(j))
print(j*2)
print(j+k)
triplet=j*3
triplet[1].first="jessica"
print(triplet)
print(j+1)
triplet=(k+j)*3
print(triplet)

