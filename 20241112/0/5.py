from math import inf

def divisor(a, b):
    if abs(b) < 1:
        raise ValueError
    c = a / b
    return -c

def proxy(fun, *args):
    try:
        return fun(*args)
    except ValueError:
        return inf
    except ZeroDivisionError:
        return inf
    

for i in range(-2, 3):
    print(proxy(divisor, 100, i))
print(proxy(divisor, 100, 0.5))
