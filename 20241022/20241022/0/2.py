def travel(n):
    for _ in range(n):
        yield "по кочкам"  # n раз выдаем "по кочкам"
    return "и в яму"       # возвращаем "и в яму" через return

def travelwrap(n):
    result = yield from travel(n)  # делегируем travel(n) и сохраняем результат
    yield result                   # выдаем возвращенное значение "и в яму"
