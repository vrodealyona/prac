def harmonic_square_sum():
    n = 1
    current_sum = 0
    while True:
        current_sum += 1 / (n ** 2)  # добавляем очередной элемент 1/n^2
        yield current_sum            # возвращаем текущую сумму
        n += 1                       # увеличиваем n для следующей итерации

sum(1 / i**2 for i in range(1, 10001))