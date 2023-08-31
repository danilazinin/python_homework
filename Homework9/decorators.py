from random import randint
from math import sqrt
from typing import Callable
import csv
import json


def save_roots(func: Callable):
    def to_json():
        params = func()
        with open('roots.json', 'w') as file:
            json.dump(params, file)
        return save_roots

    return to_json


def root_finder_decorator(func: Callable):
    params = {}

    def wrapper():
        with open('random_nums.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                params[f'{line[0]}, {line[1]}, {line[2]}'] = func(int(line[0]), int(line[1]), int(line[2]))
        return params

    return wrapper


@save_roots
@root_finder_decorator
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        root1 = ((-b) + sqrt(discr)) / (2 * a)
        root2 = ((-b) - sqrt(discr)) / (2 * a)
        return root1, root2
    elif discr == 0:
        return ((-b) + sqrt(discr)) / (2 * a)
    else:
        return 'no roots'


def generate_csv():
    with open('random_nums.csv', 'w') as file:
        csv_write = csv.writer(file)
        count = randint(100, 1000)
        for i in range(count):
            csv_write.writerow([randint(10, 100), randint(10, 100), randint(10, 100)])