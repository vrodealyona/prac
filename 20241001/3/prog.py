from math import *
def Calc(s, t, u):
    s = eval(f"lambda x: {s}")
    t = eval(f"lambda x: {t}")
    u = eval(f"lambda x, y: {u}")
    def U(x):
        return u(s(x), t(x))
    return U

st = eval(input())
F = Calc(st[0], st[1], st[2])
print(F(float(input())))
