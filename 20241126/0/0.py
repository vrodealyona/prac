import sys
with open(sys.argv[1], "rb") as f:
    data = f.read()
    ans = data[int(len(data)/2) :] + data[0 : int(len(data)/2)]
with open(sys.argv[1], 'wb') as f:
    print(ans)
    f.write(ans)
