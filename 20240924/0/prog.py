#a = eval(input())
#if not 13 in a:print("None")

#print(13 in eval(input()))

a = list(range(5, 16))
a[4:7] = list("abcdefghijk")[-5:]
print(a)

####
a = list(range(5, 17)
a[len(a): len(a)//2: -2]
a[-1: len(a)//2-1: -2]

####
for i in range(1, 10):
     for j in range(1, 10):
             print(i,"*", j, "=", i*j, sep ="",  end=" ")
     print()

####
a = eval(input())
for i in a:
	if i%2:
		break
print(i)

a = [eval(input())]
l = len(a)
while k:= eval(input()):
	a.append(k)
for i in range(0, l):
	for j in range(0, l):
		print(a[j][i], end = " ")
	print()
