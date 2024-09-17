b = 0
while a := int(input()):
	if a <= 0: 
		print(a) 
		break
	b += a
	if b > 21: 
		print(b) 
		break
