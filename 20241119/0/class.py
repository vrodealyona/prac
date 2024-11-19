class Dumper():
	def __init__(self, typ):
		self.typ = typ

	def __call__(self, fun):
		def newfun(*args):
			if not all(isinstance(i, self.typ) for i in args):
				raise TypeError
			return fun(*args)
		return newfun

@Dumper(float)
def add(x, y, z):
	return x+y+z
	
print(add(1, 2, 3))
