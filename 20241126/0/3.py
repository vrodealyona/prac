import pickle
class SerCls:
    def __init__(self, l, d, n, s):
        self.l = l
        self.d = d
        self.n = n
        self.s = s
    def __str__(self):
        return f"{self.l}, {self.d}, {self.n}, {self.s}"

ser = SerCls([1,2,3], {'1':1, '2':2}, 1234, 'ahjd')
dump = pickle.dumps(ser)
del ser
ser1 = pickle.loads(dump)
print(ser1)


