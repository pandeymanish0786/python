from random import shuffle
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
	def reset(self):
		suits=["hearts","diamonds","cubs","spade"]
		values=["a","2","3","4","5","6","7","8","9","10","j","q","k"]
		self.cards=[card(value,suit) for suit in suits for value in values]
		return self
	def count(self):
		return len(self.cards)
	def _deal(self,num):
		count=self.count()
		actual=min([count,num])
		if count==0:
			raise ValueError("all cards have been dealt")
		if actual==1:
			return [self.cards.pop()]
		cards=self.cards[-actual: ]
		self.cards=self.cards[ : -actual]
		return cards
	def shuffle(self):
		if self.count()<52:
			raise ValueError("only full deck can be shuffled")
		shuffle(self.cards)
		return(self)
	def deal_card(self):
		return self._deal(1)[0]
	def deal_hand(self,hand_size):
		return self._deal(hand_size)
my_deck=deck()
my_deck.shuffle()
for card in my_deck:
	print(card)
