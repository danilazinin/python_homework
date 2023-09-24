class NegativeValueException(Exception):

    def __str__(self):
        return f'Значение не должно быть отрицательным'


class CharsException(Exception):

    def __str__(self):
        return f'Значение должно быть онли буквы'