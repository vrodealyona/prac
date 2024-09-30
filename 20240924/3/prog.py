a = []
b = []
c = []
a.append(list(eval(input())))
n = len(a[0])
for i in range(1, n):
    a.append(list(eval(input())))

for i in range(n):
    b.append(list(eval(input())))

d = []
for i in range(n):
    for j in range(n):
        s = 0
        for k in range(n):
            s = s + a[i][k]*b[k][j]
        d.append(s)
    c.append(d)
    d = []
    print(*c[i], sep = ',')
