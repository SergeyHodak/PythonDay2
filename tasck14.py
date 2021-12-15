class DataField:
    field_description = "General"


class FirstNameField(DataField):
    field_description = "Name"


# 1. Создайте класс CityField, который наследует DataField, но поле field_description у него должно иметь значение "City".
# 2. Создайте класс SkillField, который наследует DataField, но поле field_description у него должно иметь значение "Skill".
# 3. Создайте класс RateField, который наследует DataField, но поле field_description у него должно иметь значение "Rate".
# 4. Создайте класс PhoneField, который наследует DataField, но поле field_description у него должно иметь значение "Phone".
class CityField(DataField):
    field_description = "City"


class SkillField(DataField):
    field_description = "Skill"


class RateField(DataField):
    field_description = "Rate"


class PhoneField(DataField):
    field_description = "Phone"