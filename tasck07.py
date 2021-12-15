class Developer:
    def __init__(self, name, city, skill, rate, phone):
        self.name = name
        self.city = city
        self.skill = skill
        self.rate = rate
        self.phone = phone

    # Дописать метод __str__ , класса Developer, который позволит выводить информацию из объекта
    # в формате 'Vlad Kyiv Python 1300 +380631234570'

    def __str__(self):
        return f"{self.name} {self.city} {self.skill} {self.rate} {self.phone}"


c1 = Developer("Сергей", "Днепр", "Python, Java", 0, "+380934516875")
print(c1)