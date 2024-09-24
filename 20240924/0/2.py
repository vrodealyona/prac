a = []
while k:= input():
	a.append(list(eval(k)))
for i in range(len(a)):
	for j in range(i+1, len(a)):
		a[i][j], a[j][i] = a[j][i], a[i][j]
		print(a[i][j], end = " ")
	print()
