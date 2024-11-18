from collections import UserString

class DivStr(UserString):
    def __init__(self, seq=""):
        super().__init__(seq)
    
    def __floordiv__(self, n):
        if n <= 0:
            raise ValueError("n должно быть больше нуля")
        l = len(self.data) // n
        return (self.data[i * l: (i+1) * l] for i in range(n))
    
    def __mod__(self, n):
        if n <= 0:
            raise ValueError("n должно быть больше нуля")
        l = len(self.data) - len(self.data) % n
        return DivStr(self.data[l:])

'''
a = DivStr("XcDfQWEasdERTdfgRTY")
print(* a // 4)
print(a % 4)
print(* a % 10 // 3)
print(a.lower() % 3)
print(* a[1:7] // 3)
print(a % 5 + DivStr() + a % 6)
'''
'''
empty = DivStr()
print(list(empty // 1))
print(empty % 1)
print(empty % 5)
'''
import sys
exec(sys.stdin.read())