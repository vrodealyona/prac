import math

# Словарь для хранения определённых функций
functions = {}

# Счётчики строк и функций
line_count = 0
function_count = 1  # Включая предопределённую функцию 'quit'

# Определяем функцию 'quit'
def quit_func(format_str):
    print(format_str.format(function_count, line_count))
    global running
    running = False  # Завершаем работу интерпретатора

# Добавляем 'quit' в список функций
functions['quit'] = {'params': ['format_str'], 'function': quit_func}

# Флаг для управления циклом интерпретатора
running = True

while running:
    try:
        line = input()
    except EOFError:
        break  # Завершаем работу при достижении конца ввода
    line = line.strip()
    if not line:
        continue  # Пропускаем пустые строки
    line_count += 1  # Увеличиваем счётчик обработанных строк

    if line.startswith(':'):
        # Обрабатываем определение функции
        definition = line[1:].strip()
        tokens = definition.split()
        func_name = tokens[0]
        params = tokens[1:-1]
        expression = tokens[-1]

        # Создаём код функции в виде строки
        param_list = ', '.join(params)
        func_code = f'def {func_name}({param_list}):\n    return {expression}'

        # Подготавливаем пространство имён для функции
        local_namespace = {}
        global_namespace = {'__builtins__': __builtins__, **math.__dict__}

        # Выполняем код функции
        exec(func_code, global_namespace, local_namespace)

        # Сохраняем функцию в словаре
        functions[func_name] = {'params': params, 'function': local_namespace[func_name]}
        function_count += 1  # Увеличиваем счётчик определённых функций

    else:
        # Обрабатываем вызов функции
        tokens = line.split()
        func_name = tokens[0]

        if func_name not in functions:
            print(f'Функция {func_name} не определена')
            continue

        func_def = functions[func_name]
        params = func_def['params']
        func = func_def['function']
        num_params = len(params)

        if num_params == 0:
            # Функция без параметров
            result = func()
            if result is not None:
                print(result)

        elif num_params == 1:
            # Функция с одним параметром
            arg_str = line[len(func_name):].strip()

            # Аргумент может содержать пробелы
            try:
                # Пытаемся вычислить аргумент как выражение
                arg_value = eval(arg_str, {'__builtins__': __builtins__, **math.__dict__})
            except:
                # Если не удалось, рассматриваем аргумент как строку
                arg_value = arg_str.strip('"\'')
            result = func(arg_value)
            if result is not None:
                print(result)

        else:
            # Функция с двумя или более параметрами
            args = tokens[1:]
            if len(args) != num_params:
                print(f'Функция {func_name} ожидает {num_params} аргументов, получено {len(args)}')
                continue

            arg_values = []
            for arg in args:
                try:
                    # Пытаемся вычислить аргумент как выражение
                    arg_value = eval(arg, {'__builtins__': __builtins__, **math.__dict__})
                except:
                    # Если не удалось, рассматриваем его как строку
                    arg_value = arg.strip('"\'')
                arg_values.append(arg_value)

            result = func(*arg_values)
            if result is not None:
                print(result)



