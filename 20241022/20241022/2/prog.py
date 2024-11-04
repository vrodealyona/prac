import itertools as it
def slide(seq, n):
    l = len(seq)
    i = 0
    if l < n:
        return
    while i < l:
        for x in it.islice(seq, i, i+n):
            yield x
        i += 1

import sys
exec(sys.stdin.read())