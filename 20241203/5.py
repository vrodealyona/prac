class C:
    a, b, c = input().split()
while p := input():
    match p.split():
        case [C.b]:
            print("Строка — это второе слово")
        case [C.a, *_] as wrds if "yes" in wrds:
            print("Строка начинается на первое слово, и в ней есть слово 'yes'")
        case [C.c, *_, C.b]:
            print("Строка начинается на третье, а заканчивается на второе слово")
        case _:
            print("None")
