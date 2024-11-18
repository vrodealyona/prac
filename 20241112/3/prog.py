class Undead(Exception):
    pass
class Skeleton(Undead):
    pass
class Zombie(Undead):
    pass
class Ghoul(Undead):
    pass

def necro(a):
    if a % 3 == 0:
        raise Skeleton("Skeleton")
    elif a % 3 == 1:
        raise Zombie("Zombie")
    else:
        raise Ghoul("Ghoul")
    
x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")
