class DataField:
    field_description = 'General'


# Создайте класс FirstNameField, который наследует DataField, но поле field_description у него
# должно иметь значение 'Name'.
class FirstNameField(DataField):
    field_description = 'Name'