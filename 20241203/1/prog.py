import sys
class dump(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for name, method in attrs.items():
            if callable(method):
                def wrap(method, name):
                    def wrapper(self, *args, **kwargs):
                        print(f"{name}: ({args}, {kwargs})")
                        return method(self, *args, **kwargs)
                    return wrapper
                
                new_attrs[name] = wrap(method, name)
            else:
                new_attrs[name] = method
        return super().__new__(cls, name, bases, new_attrs)

exec(sys.stdin.read())