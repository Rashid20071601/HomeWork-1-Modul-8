def add_everything_up(a, b):
    # Пытаемся сложить два аргумента. Если они совместимы по типу, результат будет числовым или строковым.
    try:
        return a + b
    # Если возникает ошибка типов (например, попытка сложить число и строку),
    # аргументы преобразуются в строки и выполняется их конкатенация.
    except TypeError:
        return str(a) + str(b)

# Пример с числом и строкой. В случае ошибки типов, происходит конкатенация.
print(add_everything_up(123.456, 'строка'))  # '123.456строка'

# Пример с числом и строкой. Ожидается, что оба аргумента будут приведены к строкам и конкатенированы.
print(add_everything_up('яблоко', 4215))  # 'яблоко4215'

# Пример с двумя числами. Сначала происходит сложение, затем результат округляется до трех знаков после запятой.
print(round(add_everything_up(123.456, 7), 3))  # 130.456