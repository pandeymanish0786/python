print("enter 1 for add  ")
print("enter 2 for sub  ")
print("enter 3 for multiply  ")
print("enter 4 for  div  ")
print("enter 5 for power  ")
print("enter 6 for quotient  ")
x=input("enter your choice")
print("enter the calue of a and b")
a=input()
b=input()
if(int(x)==1):
	def add(a,b):
		return a+b
	add(a,b)
elif(x==2):
	def sub(a,b):
		return a-b
		sub(a,b)
elif(x==3):
	def multiply(a,b):
		return a*b
	multiply(a,b)
elif(x==4):
	def div(a,b):
		return a/b
	div(a,b)
elif(x==5):
	def power(a,b):
		return a**b
	power(a,b)
elif(x==6):
	def quotient(a,b):
		return a//b
	quotient(a,b)
else:
	print("invalid choice")