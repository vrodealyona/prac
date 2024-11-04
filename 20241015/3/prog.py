from collections import Counter
w = int(input())
lines = []
while True:
    line = input().strip()
    if line == "":
        break
    lines.append(line)

text = ' '.join(lines)
text = ''.join([ch if ch.isalpha() else ' ' for ch in text]).lower()

words = text.split()
words = [word for word in words if len(word) == w]
wrd = Counter(words)

if wrd:
    m = max(wrd.values())
    print(' '.join(word for word, count in wrd.items() if count == m))

