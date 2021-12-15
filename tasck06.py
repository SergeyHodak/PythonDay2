class Developer:
    def __init__(self, name, phone):
        self.name = name
        self.city = 'Kyiv'
        self.skill = 'Python'
        self.rate = 1300
        self.phone = phone


user = Developer('Vlad', '+380631234570')
# F-строки -позволяет выводить инфу в одну строку
# Задание. Задать значение переменной out, которое позволит вывести в консоль значения всех полей объекта developer
# в формате 'Vlad Kyiv Python 1300 +380631234570'
out = f"{user.name} {user.city} {user.skill} {user.rate} {user.phone}"
print(out)
