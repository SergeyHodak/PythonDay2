class Developer:
    def __init__(self):
        self.fields = []

    def add(self, field_item):
        self.fields.append(field_item)

    def delete(self, idx):
        # Доработайте метод delete класса Developer так, чтобы он удалял элемент с индексом idx
        # из списка записей, который хранится в поле fields.
        self.fields.pop(idx)