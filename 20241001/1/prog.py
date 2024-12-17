def Pareto(*pairs):
    res = []
    for x in pairs:
        for y in pairs:
            if (x[0] <= y[0]) and (x[1]<=y[1]) and ((x[0] != y[0]) or (x[1] != y[1])):
                break
        else:
            res.append(x)
    return tuple(res) if len(res)>1 else (res[0])

print(Pareto(*eval(input())))
