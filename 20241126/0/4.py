import struct
import random

with open("aoaoao", "wb") as f:
    for _ in range(10):
        f.write(struct.pack('f3si', random.random(), bytes((random.randrange(2, 5), random.randrange(2, 5), random.randrange(2, 5))),  random.randrange(10000)))
