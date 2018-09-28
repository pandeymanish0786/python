import unittest
from activities import eat,nap
class activity_tests(unittest.Testcase):
	def test_eat_healthy(self):
		""" eat should have +ve msg for healthy eating"""
		self.AssertEqual(
			eat("brocolui",is_healthy=True),
			"i'm earting brocoli ,because my body is a temple"
		)
	def test_eat_unhealthy(self):
		self.AssertEqual(
			eat("pizza",is_healthy=False),"i'm eating pizza ,because yolo"
		)
	def test_short_nap(self):
		self.AssertEqual(
			nap(1),
			"i'm felling represhed after my 1 hour nap"
		)