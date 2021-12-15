def validate(value):
    try:
        out = float(value)
    except ValueError:
        out = None
    return out
# Реализуйте функцию validate, которая с помощью блока try проверяет на возникновение исключения приведения к типу
# float значения параметра value. При возникновения исключения ValueError переменная out получает значение None,
# при отсутствии исключения получает значение float(value).