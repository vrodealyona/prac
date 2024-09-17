a = int(input())
A = "-"
B = "-"
C = "-"
if not(a%2) and not (a%25):
	A = "+"
elif (a%2) and not (a%25):
	B = "+"
if not (a%8):
	C = "+"
print("A", A, "B", B, "C", C)
