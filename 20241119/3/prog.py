alph = "abcdefghijklmnopqrstuvwxyz"
class Alpha:
    __slots__ = tuple(alph)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if key in self.__slots__:
                setattr(self, key, val)
            else:
                raise AttributeError(f"Invalid field: {key}")
    def __str__(self):
        return ", ".join(f"{k}: {getattr(self, k)}" for k in sorted(self.__slots__) if hasattr(self, k))
    
class AlphaQ:
    def __init__(self, **kwargs):
        self._fields = {}
        for key, val in kwargs.items():
            if key in alph:
                self._fields[key] = val
            else:
                raise AttributeError(f"Invalid field: {key}")
            
    def __getattr__(self, name):
        if name in self._fields:
            return self._fields[name]
        raise AttributeError(f"{name} does not exist")
    
    def __setattr__(self, name, val):
        if name == "_fields" or name in alph:
            if name == "_fields":
                super().__setattr__(name, val)
            else:
                self._fields[name] = val
        else:
            raise AttributeError(f"Invalid field: {name}")
    def __str__(self):
        return ", ".join(f"{k}: {v}" for k, v in sorted(self._fields.items()))
    
import sys
exec(sys.stdin.read())