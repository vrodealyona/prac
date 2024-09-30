a = []
b = []
c = []
a.append(list(eval(input())))
n = len(a[0])
for i in range(1, n):
    a.append(list(eval(input())))
print(a)
for i in range(n):
    b.append(list(eval(input())))
print(b)
c = a
for i in range(n):
    for j in range(n):
        c[i][j] = 0
        for k in range(n):
            c[i][j] = c[i][j] + a[i][k]*b[k][j]
            print(a[i][k]*b[k][j], c[i][j], end = "|")
        print()
    print(*c[i], sep=",")
