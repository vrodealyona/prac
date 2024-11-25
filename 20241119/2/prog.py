class Num:
    def __init__(self, val=0):
        self.val = val

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.val, 0)
    
    def __set__(self, instance, value):
        if type(value) is float or type(value) is int:
            instance.__dict__[self.val] = value
        elif hasattr(value, '__len__'):
            instance.__dict__[self.val] = len(value)

import sys
exec(sys.stdin.read())