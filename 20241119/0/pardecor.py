def istype(typ):
	def decorator(fun):
		def newfun(*args):
			if all(isinstance(i, typ) for i in args):
				return [fun(*args)]
			else:
				return "Buba"
		return newfun
	return decorator

@istype(int)
def simplefun(N):
	return N*2+1

print(*simplefun(5.1))
