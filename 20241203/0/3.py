class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
             cls._instance = super().__call__(*args, **kw)
        return cls._instance


class Doubleton(type):
    _instance = []
    _count = 0
    def __call__(cls, *args, **kw):
        if len(cls._instance) < 2:
            cls._instance.append(super().__call__(*args, **kw))
        cls._count +=1
        return cls._instance[cls._count % 2 - 1]

class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")