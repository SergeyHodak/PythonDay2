class IncorrectInput(Exception):
    pass


class RateField:
    field_description = "Rate"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        try:
            self.value = float(value)
        except ValueError:
            raise IncorrectInput(f"{value} - не возможно трансформировать в float")

# В итоговом проекте класс RateField отвечает за работу с полем, которое хранит уровень оплаты разработчика.
# В этом классе реализован метод validate, в котором получаемое значение value
# конвертируется во float и сохраняется в поле self.value.
# В случае, если переданное значение value
# не может быть сконвертировано во float (например, пользователь ввел символ), вызывается исключение
# ValueError.
# Обработайте исключения ValueError в блоке try ... except ...  так, чтобы при возникновении ошибки
# ValueError вызывался класс IncorrectInput, реализующий собственное исключение. Строку, которую возвращает IncorrectInput укажите по собственному желанию.