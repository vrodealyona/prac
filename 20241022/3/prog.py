from itertools import product

#n = int(input())
print(*filter(lambda y: y.count('TOR') == 2, sorted(list(''.join(x) for x in product('TOR', repeat=int(input()))))))