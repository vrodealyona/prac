a, b = 20, 50
print([i for i in range(a//2*2+1, b, 2) if i%2 and "3" not in str(i)])
