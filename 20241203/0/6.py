import inspect

class C:
    a: int 
    def __init__(self, val):
        if not isinstance(val, inspect.get_annotations(self.__class__)['a']):
            raise TypeError("sjas")
        self.a = val
    
c = C(9)
b = C(1.23)