#print("Not Em" if eval(input()) else "Empty")

#a, b = eval(input())
#print(b and (a/b) or a)

#a, b, c = eval(input())
#if a> 0 and b > 0 and c > 0:
#	print("Tre" if (a+b>c and b+c>a and a+c>b) else "Not tre")

#i = 1
#k = 0
#a = int(input())
#while(a):
#	if a == i: k = k + 1
#	i = i+1
#	a = int(input())
#
#print(k)

#while a := eval(input()):
#	if not(a % 2 ): print(a)

#while a := eval(input()):
#	if not(a % 2 ): print(a)
#	elif a == 13: print("Oops!") break
#else: print("Winner!")

a = eval(input())
match a:
	case 1: print("1(one)")
	case 2: print("2(two)")
	case 3: print("3(three)")
	case var if var % 2:
		print("- это много")
	case var:
		print("чётное")
