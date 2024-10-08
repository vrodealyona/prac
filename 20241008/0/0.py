from decimal import Decimal as dec
from fractions import Fraction as frac

def multiplier(x, y, Type):
	return Type(x)*Type(y)

def esum(N, one):
	sum = one
	for i in range(1, N+1):
		one = one/i
		sum = one + sum
	return sum

>>> def scale(a, b, A, B, x):
...     x = (B-A)/(b-a)*x + A
...     return x
