class dump(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for name, method in attrs.items():
            if callable(method):
                def wrapper(*args, **kwargs):
                    print(f"{name}: ({args}, {kwargs})")
                    return method(*args, **kwargs)
                new_attrs[name] = wrapper
            else:
                new_attrs[name] = method
        return super().__new__(cls, name, bases, new_attrs)


class C(metaclass=dump):
    def __init__(self, val):
        self.val = val

    def add(self, other, another=None):
        return self.val + other + (another or self.val)

c = C(10)
print(c.add(9))
print(c.add(9, another=10))


