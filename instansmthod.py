class user:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
	def full_name(self):
		return f"{self.first} {self.last}"
	def initials(self):
		return f"{self.first[0]}. {self.last[0]}."
	def likes(self,things):
		return f"{self.first} likes {things}"
	def is_senior(self):
		return self.age>=65
	def birthday(self):
		self.age+=1
		return f"happy{self.age}th ,{self.first}"
	def say_hi():
		print("hello!")
user1=user("joe","smith",68)
user2=user("blana","lopez",41)
print(user1.likes("ice creams"))
print(user2.initials())
print(user1.is_senior())
print(user2.age)
print(user1.birthday())
user.say_hi()

