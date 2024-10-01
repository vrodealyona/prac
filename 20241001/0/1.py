def rbin(n, a = [], i = 1):
	if n == 0:
		print(*a, sep = "")
	else:
		rbin(n-1, a + [i], 0)
		rbin(n-1, a + [i], 1)
		

rbin(5, [], 1)
