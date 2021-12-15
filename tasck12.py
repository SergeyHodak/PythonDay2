class Developer:
    def __init__(self):
        self.fields = ['name','city','email']

    def add(self, field_item):
        self.fields.append(field_item)

    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    def update(self, idx, value):
        # Доработайте метод update класса Developer так, чтобы он обновлял значение элемента
        # списка fields (номер елемента передается в параметре idx) на
        # значение, переданное в параметре value.
        self.fields[int(idx)] = value