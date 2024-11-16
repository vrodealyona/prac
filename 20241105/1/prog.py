class Omnibus:
    _count = {}

    def __init__(self):
        self._set = set()  # Храним атрибуты, установленные для этого объекта

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
            return

        # Если атрибут уже установлен, просто обновляем значение
        if name not in self._set:
            self._set.add(name)
            Omnibus._count[name] = Omnibus._count.get(name, 0) + 1

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"'{name}' is not a valid attribute")
        return Omnibus._count.get(name, 0)

    def __delattr__(self, name):
        if name.startswith('_'):
            return
        
        if name in self._set:
            self._set.remove(name)
            Omnibus._count[name] -= 1
            if Omnibus._count[name] == 0:
                del Omnibus._count[name]

              
import sys
exec(sys.stdin.read())
