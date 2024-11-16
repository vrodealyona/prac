def is_intersecting(a1, a2, b1, b2):
    f1 = (a2[1] - a1[1])*(b1[0] - a1[0]) - (a2[0] - a1[0])*(b1[1] - a1[1])
    f2 = (a2[1] - a1[1])*(b2[0] - a1[0]) - (a2[0] - a1[0])*(b2[1] - a1[1])
    f3 = (b2[1] - b1[1])*(a1[0] - b1[0]) - (b2[0] - b1[0])*(a1[1] - b1[1])
    f4 = (b2[1] - b1[1])*(a2[0] - b1[0]) - (b2[0] - b1[0])*(a2[1] - b1[1])

    if f1*f2<0 and f3*f4<0:
        return True
    return False

class Triangle:
    def __init__(self, a, b, c):
        self.x1 = list(a)
        self.x2 = list(b)
        self.x3 = list(c)
        self.a = ((self.x1[0] - self.x2[0])**2 + (self.x1[1] - self.x2[1])**2)**0.5 
        self.b = ((self.x1[0] - self.x3[0])**2 + (self.x1[1] - self.x3[1])**2)**0.5 
        self.c = ((self.x3[0] - self.x2[0])**2 + (self.x3[1] - self.x2[1])**2)**0.5 
    def __abs__(self):
        self.s = 0
        if 2*max(self.a, self.b, self.c) < self.a + self.b + self.c:
            p = (self.a + self.b + self.c)/2
            self.s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return self.s
    def __bool__(self):
        return abs(self) != 0
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __contains__(self, other):
        if bool(other) == False:
            return True
        if self.x1 == other.x1 and self.x2 == other.x2 and self.x3 == other.x3:
            return True
        if other < self:
            for i in (other.x1, other.x2, other.x3):
                f1 = (self.x1[0] - self.x3[0])*(i[1] - self.x3[1]) - (self.x1[1] - self.x3[1])*(i[0] - self.x3[0])
                f2 = (self.x3[0] - self.x2[0])*(i[1] - self.x2[1]) - (self.x3[1] - self.x2[1])*(i[0] - self.x2[0])
                f3 = (self.x2[0] - self.x1[0])*(i[1] - self.x1[1]) - (self.x2[1] - self.x1[1])*(i[0] - self.x1[0])
                if not((f1>=0 and f2>=0 and f3>=0) or (f1<=0 and f2<=0 and f3<=0)):
                    return False
            return True
        else:
            return False    
    def __and__(self, other):
        if self and other:
            if any(i == j for i in (self.x1, self.x2, self.x3) for j in (other.x1, other.x2, other.x3)):
                return True
            if (self in other) or (other in self):
                return True
            for a1, a2 in ((self.x1, self.x2), (self.x2, self.x3), (self.x3, self.x1)):
                for b1, b2 in ((other.x1, other.x2), (other.x2, other.x3), (other.x3, other.x1)):
                    if is_intersecting(a1, a2, b1, b2):
                        return True
        return False
    
'''
r = Triangle((4, 2), (1, 3), (2, 4))
s = Triangle((1, 1), (3, 1), (2, 2))
t = Triangle((0, 0), (2, 3), (4, 0))
o = Triangle((1, 1), (2, 2), (3, 3))
t1 = Triangle((0, 5), (5, 0), (-5, 0))
t2 = Triangle((5, 1), (-5, 1), (0, -5))
print(*(f"{n}({bool(x)}):{round(abs(x), 3)}" for n, x in zip("rsto", (r, s, t, o))))
print(f"{s < t=}, {o < t=}, {r < t=}, {r < s=}")
print(f"{s in t=}, {o in t=}, {r in t=}, {t in r=}, {t in s=}, {t in o=}")
print(f"{r & t=}, {t & r=}, {s & r=}, {o & t=}, {t1 & t2=}")
'''
import sys
exec(sys.stdin.read())

