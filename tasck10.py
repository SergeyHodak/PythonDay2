class Developer:
    def __init__(self):
        self.fields = []

    # Доработайте метод add класса Developer так, чтобы он добавлял переданный параметр field_item
    # в конец списка self.fields.
    def add(self, field_item):
        self.fields.append(field_item)