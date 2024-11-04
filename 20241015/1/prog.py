s = input().lower()
w = set()
for i in range(1, len(s)):
    if (s[i-1].isalpha()) and (s[i].isalpha()):
        w.add(s[i-1] + s[i])

#print(w)
print(len(w))