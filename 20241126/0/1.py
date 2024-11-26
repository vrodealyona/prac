import sys
with open(sys.argv[1], "rt") as f:
    s = f.readlines()

for i in range(len(s)//3):
    if s[i] == '\n':
        break
else:
    i += 1
print(s[:i])