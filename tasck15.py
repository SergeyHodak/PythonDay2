out = ''
value = 'f'
try:
    value = float(value)
except ValueError:
    out = f"value {value} can't be converted to float"
if out:
    print(out)
# Реализуйте обработку исключения ValueError для блока try, при срабатывании которого переменной out присваивается
# значение value {value} can't be converted to float.
