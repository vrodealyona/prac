a = [[],[]]
for k in eval(input()):
    a[0].append(k)
    a[1].append(k*k%100)
for i in range(len(a[0])-1):
    for j in range(i+1, len(a[0])):
        if a[1][i] > a[1][j]:
            a[0][i], a[0][j] = a[0][j], a[0][i]
            a[1][i], a[1][j] = a[1][j], a[1][i]

print(a[0])
