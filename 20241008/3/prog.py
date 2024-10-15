def rotate(cont):
    w = len(cont[0]) - 2
    h = len(cont) - 2

    rot = [['#'] * (h+2)]
    for i in range(w):
        t = ['#']
        for j in range(1, h+1):
            t.append(cont[j][i+1])
        t.append('#')
        rot.append(t)
    rot.append(['#'] * (h+2))

    return rot

def fluid(rotated):
    width = len(rotated[0]) - 2  
    height = len(rotated) - 2    
    
    total_volume = width * height  
    water = 0
    
    for row in range(1, height + 1):
        water += rotated[row].count('~')
    
    if height != 0:
        water_layers = water // width
        if water % width > 0:
            water_layers += 1
    else:
        water_layers = 0

    for row in range(1, height + 1):
        if row <= height - water_layers:
            rotated[row] = ['#'] + ['.'] * width + ['#'] 
        else:
            rotated[row] = ['#'] + ['~'] * width + ['#'] 

def pr(rot):
    for _ in rot:
        print(''.join(_))

def count_fluids(cont):
    gas = 0
    water = 0
    for row in cont:
        gas += row.count('.')
        water += row.count('~')
    return gas, water

def build(gas, water, total):
    g_l = round(gas/total * 20)
    w_l = 20 - g_l

    gs = '.' * g_l
    wtr = '~' * w_l

    g_f = f"{gas}/{total}"
    w_f = f"{water}/{total}"

    mlen = max(len(g_f), len(w_f))

    print(f"{gs:<{20}} {g_f:>{mlen}}")
    print(f"{wtr:<{20}} {w_f:>{mlen}}")

def fun():
    cont = []
    while True:
        line = input()
        if not line:
            break
        line = line.strip()
        cont.append(list(line))

    rot = rotate(cont)
    fluid(rot)
    total = (len(rot) - 2) * (len(rot[0]) - 2)
    gas, water = count_fluids(rot)

    pr(rot)
    build(gas, water, total)

fun()
