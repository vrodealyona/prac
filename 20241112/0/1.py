class A:
	def __init__(self, val):
		self.val = val
	def __add__(self, other):
		return self.__class__(self.val + other.val)
		
class B(A):
	def __sub__(self, other):
		return B(self.val - other.val)
