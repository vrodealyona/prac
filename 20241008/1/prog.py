from fractions import Fraction as frac

def parse(s):
    t = []
    s = s.split(', ')
    t.append(frac(s[0]))
    t.append(frac(s[1]))
    t.append(int(s[2]))
    t.append([frac(s[i]) for i in range(3, 4+t[2])])
    t.append(int(s[3+t[2]]))
    l = len(t)
    t.append([frac(s[i]) for i in range(l+2, len(s))])

    return t

def evaluate(coeff, x):
    d = len(coeff) - 1
    s = 0
    for c in coeff:
        s = s*x + c
        #print(s)
    return s

def check(st):
    st = parse(st)
    #print(st)
    s, w, deg_A, coeffs_A, deg_B, coeffs_B = st[0], st[1], st[2], st[3], st[4], st[5]
    A_s = evaluate(coeffs_A, s)
    B_s = evaluate(coeffs_B, s)

    #print(A_s, B_s)

    if B_s == 0:
        return False

    return frac(A_s/B_s) == w

print(check(input()))