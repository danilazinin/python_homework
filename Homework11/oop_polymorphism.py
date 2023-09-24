import time
import numpy as np
from exceptions import NegativeValueException, CharsException


class MyString(str):
    """ Class MyString extends class str"""

    def __init__(self, author_name, string):
        if isinstance(author_name, str):
            self.name = author_name
        else:
            raise CharsException
        if isinstance(string, str):
            self.string = string
        else:
            raise CharsException

    def __new__(cls, author_name, string):
        instance = super().__new__(cls)
        instance.name = author_name
        instance.string = string
        seconds = time.time()
        instance.time_ = time.ctime(seconds)
        return instance

    def __str__(self):
        return f'Created instance of MyString, author name - {self.name}, string text - {self.string}'


class Archive:
    """Class Archive has a number and string attributes and save it to lists"""
    object = None

    def __init__(self, number, string):
        self.num = number
        self.string = string

    def __new__(cls, *args, **kwargs):
        if not cls.object:
            cls.object = super().__new__(cls)
            cls.object.text = []
            cls.object.nums = []
        else:
            cls.object.text.append(cls.object.string)
            cls.object.nums.append(cls.object.num)
        return cls.object

    def __str__(self):
        return f'Создан объект с текстом {self.text} и числом {self.num}'

    def __repr__(self):
        return f'Archive({self.text}, {self.num})'


class Rectangle:
    """Class creates a rectangle and has parameters length and width"""

    def __init__(self, length, width=None):
        if length < 0:
            raise NegativeValueException()
        else:
            self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def perimeter_calculation(self):
        return (self.length + self.width) * 2

    def area_calculation(self):
        return self.length * self.width

    def __sub__(self, other):
        perim1 = self.perimeter_calculation()
        perim2 = other.perimeter_calculation()
        if perim1 < perim2:
            res = perim2 - perim1
        else:
            res = perim1 - perim2
        rect_sum = res // 2
        length = rect_sum - 1
        heigth = 1
        return Rectangle(length, heigth)

    def __add__(self, other):
        perim = self.perimeter_calculation() + other.perimeter_calculation()
        rect_sum = perim // 2
        length = rect_sum - 1
        heigth = 1
        return Rectangle(length, heigth)

    def __str__(self):
        return f'Rectangle parameters: width -> {self.width}, length -> {self.length}'

    def __lt__(self, other):
        return self.area_calculation() < other.area_calculation()

    def __eq__(self, other):
        return self.area_calculation() == other.area_calculation()

    def __ne__(self, other):
        return self.area_calculation() != other.area_calculation()

    def __le__(self, other):
        return self.area_calculation() <= other.area_calculation()

    def __gt__(self, other):
        return self.area_calculation() > other.area_calculation()

    def __ge__(self, other):
        return self.area_calculation() >= other.area_calculation()


rect1 = Rectangle(-1, 3)
rect2 = Rectangle(3, 9)


class Matrix:
    """Creating of matrix"""

    def __init__(self, matrix: [[]]):
        self.matrix = matrix

    def __str__(self):
        return f'matrix - {self.matrix}'

    def __add__(self, other):
        return np.add(self.matrix, other.matrix)

    def __mul__(self, other):
        return np.dot(self.matrix, other.matrix)

    def __lt__(self, other):
        return self.matrix < other.matrix