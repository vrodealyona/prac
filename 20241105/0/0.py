class Rectangle:
	rectcnt = 0
	def __init__(self, x1, y1, x2, y2):
		self.__class__.rectcnt += 1
		setattr(self, "rect_"+str(self.rectcnt), self.rectcnt)
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
	def __str__(self):
		return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}), {self.rectcnt}"
	def __abs__(self):
		return (self.x2-self.x1)*(self.y2-self.y1)
	def __lt__(self, other):
		s1 = abs(self)
		s2 = abs(other)
		return s1<s2 
	def __eq__(self, other):
		s1 = abs(self)
		s2 = abs(other)
		return s1==s2
	def __mul__(self, num):
		self.x1 *= num
		self.x2 *= num
		self.y1 *= num 
		self.y2 *= num
		return self
	__bool__ = __abs__ != 0
	def __rmul__(self, num):
		self.__mul__(num)
		return self
	#def __bool__(self):
	#	return abs(self) != 0
	def __del__(self):
		self.__class__.rectcnt -= 1
		print(self.__class__.rectcnt)
	def __getitem__(self, i):
		return((self.x1,self.y1),(self.x1,self.y2),(self.x2,self.y2),(self.x2,self.y1))[i]
		
