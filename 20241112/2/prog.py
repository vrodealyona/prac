class InvalidInput(Exception):
    pass
class BadTriangle(Exception):
    pass
def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
        a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        b = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
        c = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
        if 2*max(a, b, c) >= (a + b + c):
            raise BadTriangle("Not a triangle")
        s = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
        if s == 0:
            raise BadTriangle("Not a trianglefsf")
        else:
            return round(s, 2)
    
    except (SyntaxError, NameError, TypeError, ValueError):
        raise InvalidInput("Invalid input")
    

while True:
    inStr = input()
    try:
        result = triangleSquare(inStr)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{result:.2f}")
        break