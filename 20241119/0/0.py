def isint(f):
	def newfun(*args):
		for i in args:
			if not type(i) is int:
				raise TypeError("not int")
		print(">", *args)
		res = f(*args)
		print("<", res)
		return res
	return newfun

@isint
def fun(a,b):
	return a*2+b

print(fun(1.2,3))
