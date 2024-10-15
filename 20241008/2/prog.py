from math import *
def scale(a, b, A, B, x):
    return (B-A) * (x-a) / (b - a) + A


s = input().split()

def fun(x):
    return eval(s[4])

#print(sin(45))
def graph(w, h, a, b):
    screen = [[" "]*w for _ in range(h)]
    y_l = []
    for i in range(w):
        x = scale(0, w, a, b, i)
        y_l.append(fun(x))
    y_max = max(y_l)
    y_min = min(y_l)

    for i in range(w):
        s = scale(y_min, y_max, 0, h-1, y_l[i])
        screen[round(s)][i] = "*"
    screen.reverse()
    print("\n".join(["".join(s) for s in screen]))

graph(int(s[0]), int(s[1]), float(s[2]), float(s[3]))