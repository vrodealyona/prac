def sumn(n):
    d = 0
    while n > 0:
        d = d + n % 10
        n = n // 10
    return d

n = int(input())
i = n
n = n + 2
while i <= n:
    j = n - 2
    while j <= n:
        print(i, "*", j, "=", end = " ")
        k = i * j
        if sumn(k) == 6:
            print(":=)", end = " ")
        else:
            print(k, end = " ")
        j += 1
    print()
    i += 1
