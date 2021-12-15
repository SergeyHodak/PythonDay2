class Developer:
    def __init__(self):
        self.fields = []

    def __contains__(self, item: str):
        # Допишите элементы метода __contains__, который должен проверить, содержит ли хоть один элемент
        # списка self.fields значение item.
        for param in self.fields:
            if item in param:
                return True
        return False
