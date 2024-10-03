def sub(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    
    if isinstance(a, (tuple, list)) and isinstance(b, (tuple, list)):
        res = [i for i in a if i not in b]
        return type(a)(res)

s = eval(input())
print(sub(s[0], s[1]))
