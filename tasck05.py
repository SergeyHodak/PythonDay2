class Developer:
    def __init__(self, name, phone):
        # Допишите метод __init__ так чтобы: 1. При создании все экземпляры класса Developer получали
        # значения по умолчанию для полей city ('Kyiv'), skill ('Python') и rate (1300), а так же
        # 2. Значения полей name и phone задаются при создании объекта
        self.city ='Kyiv'
        self.skill = 'Python'
        self.rate = 1300
        self.name = name
        self.phone = phone


user = Developer('Vlad', '+380631234570')