from timeit import *
def f():
	s = input().split()
	sl = {}
	for w in s:
		sl.setdefault(w, 0)
		sl[w] += 1
	return sl

from collections import Counter

def C():
	return Counter(input().split())

T = Timer(f, globals=None)
print(T.autorange())

T = Timer(C, globals=None)
print(T.autorange())

#другая задача
#" ".join({w:1 for w in "abc def abc qwert def".split()})

