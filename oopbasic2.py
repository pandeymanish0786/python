class  person:
	def __init__(self):
		self.name="tony"
		self._secret="hi"
		self.__msg="i like u"
p=person()
print(p.name)
print(p._secret)
print(p._person__msg)
