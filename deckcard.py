class card:
	def __init__(self,value,suit):
		self.value=value
		self.suit=suit
	def __repr__(self):
		return f"{self.value} of {self.suit}"
class deck:
	def __init__(self):
		suits=["hearts","diamonds","cubs","spade"]
		values=["a","2","3","4","5","6","7","8","9","10","j","q","k"]
		self.cards=[card(value,suit) for suit in suits for value in values]
	def __repr__(self):
		return f"deck of {self.count()} cards"
	def count(self):
		return len(self.cards)
	def _deal(self,num):
		count=self.count()
		actual=min([count,num])
		if count==0:
			raise ValueError("all cards have been dealt")
		cards=self.cards[-actual: ]
		self.cards=self.cards[ : -actual]
		return cards
	def deal_card(self):
		return self._deal(1)[0]
	def deal_hand(self,hand_size):
		return self._deal(hand_size)
	def suffle(self):
		if self.count()<52:
			raise ValueError("only full deck can be suffled")
			shuffle(self.cards)
			return self
d=deck()
d.suffle()
card=d.deal_card()
print(card)
hand=d.deal_hand(50)
card2=d.deal_card()
print(card2)
print(d.cards)
card2=d.deal_card()

