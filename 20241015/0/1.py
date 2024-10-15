import string
def f():
	alp = set(string.ascii_lowercase)
	gl = set('euioa')
	s = input()
	sg = alp - gl
	return len(gl & s), len(sg & s)

from timeit import *
T = Timer(f, globals = globals)
print(T().autorange())
