arr = []
while a := input():
	arr.append(eval(a))

for i in range(1, len(arr)-1):
	if len(arr[0]) != len(arr[i]): 
		print("False") 
		break
else: 
	if len(arr[0]) == len(arr): print("True")
	else: print("False") 
