class Developer:
    def __init__(self):
        self.fields = []

    def add(self, field_item):
        self.fields.append(field_item)

    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    def update(self, idx, value):
        idx = int(idx)
        self.fields[idx] = value

class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}:{self.value}"

class FirstNameField(DataField):
    field_description = "Name"

class CityField(DataField):
    field_description = "City"

class SkillField(DataField):
    field_description = "Skill"

class PhoneField(DataField):
    field_description = "Phone"

class RateField(DataField):
    field_description = "Rate"


developer1 = Developer()
developer1.add(FirstNameField("Vlad"))
developer1.add(CityField("Kyiv"))
developer1.add(SkillField("Python"))
developer1.add(PhoneField("+3806312345670"))
developer1.add(RateField(1300))

developer2 = Developer()
developer2.add(FirstNameField("Max"))
developer2.add(CityField("Lviv"))
developer2.add(SkillField("Python"))
developer2.add(PhoneField("+3806312345671"))
developer2.add(RateField(1200))

developer3 = Developer()
developer3.add(FirstNameField("Ivan"))
developer3.add(CityField("Kyiv"))
developer3.add(SkillField("Python"))
developer3.add(PhoneField("+3806312345672"))
developer3.add(RateField(2800))

print(developer1.fields[0])
print(developer1.fields[1])
print(developer1.fields[2])
print(developer1.fields[3])
print(developer1.fields[4])

print(developer2.fields[0])
print(developer2.fields[1])
print(developer2.fields[2])
print(developer2.fields[3])
print(developer2.fields[4])

print(developer3.fields[0])
print(developer3.fields[1])
print(developer3.fields[2])
print(developer3.fields[3])
print(developer3.fields[4])

# По аналогии с нашими печеньками, опишите данные трех разработчиков:
# 1. Разработчик developer1 с данными 'Vlad', 'Kyiv', 'Python', '+3806312345670', 1300.
# 2. Разработчик developer2 с данными 'Max', 'Lviv', 'Python', '+3806312345671', 1200.
# 3. Разработчик developer3 с данными 'Ivan', 'Kyiv', 'Python', '+3806312345672', 2800.
