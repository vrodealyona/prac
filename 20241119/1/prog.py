def objcount(cls):
    class Decor(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            Decor.counter += 1
            super().__init__(*args, **kwargs)
        
        def __del__(self):
            if hasattr(super(), "__del__"):
                super().__del__()
            Decor.counter -= 1
    return Decor

import sys
exec(sys.stdin.read())