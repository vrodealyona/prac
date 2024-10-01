def average(a, *args):
     k = 1
...  s = a
...  for i in args:
..           k += 1
...          s += i
...  s = s/k
..   return s

sorted(range(20), key = lambda x: x%5)

def S(f, g):
...     def fun(x):
...         return f(x)+g(x)
...     return fun

def MINF(*funs):
	return lambda x: min(f(x) for f in funs)


def MINF(*funs):
	def g(x):
		return min([f(x) for f in funs ])
	return g
	
def F():
	def fun():
		return x
	print(fun.__closure__[0])
	x = 3
	print(fun.__closure__[0].cell_contents)
	return fun
	
res = F()
print(res())


dwuc = lambda a, b: lambda x: a*x+b

