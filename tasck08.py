class Developer:
    def __init__(self):
        self.fields = []


developer = Developer()
# 1. Добавьте 5 значений полю fields  созданного объекта developer  ('name', 'city', 'developer_skill',
# 'rate', 'phone').
# 2. Измените значение элемента 'developer_skill' списка fields на 'skill'
# 3. Удалите 2 последних элемента списка fields
# 4. Присвойте переменной out первые три значения списка fields через пробел в формате name city skill
# (рекомендуется использовать функционал f-строк)
developer.fields.append('name')
developer.fields.append('city')
developer.fields.append('developer_skill')
developer.fields.append('rate')
developer.fields.append('phone')
developer.fields[2] = 'skill'
developer.fields.pop(4)
developer.fields.pop(3)
out = f"{developer.fields[0]} {developer.fields[1]} {developer.fields[2]}"
print(out)