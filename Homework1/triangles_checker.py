from logger import get_logger
import argparse

parser = argparse.ArgumentParser('Triangles parser')
parser.add_argument('a', type=int, help='Input value a')
parser.add_argument('b', type=int, help='Input value b')
parser.add_argument('c', type=int, help='Input value c')
args = parser.parse_args()


def check_triangle(a, b, c):
    # a = int(input('Введите сторорону а: '))
    # b = int(input('Введите сторону b: '))
    # c = int(input('Введите сторону с: '))
    log = get_logger()
    if a == b == c:
        log.info('Равносторонний')
        return 'Треугольник равносторонний'
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        log.error('Треугольник не существует')
        return 'Такой треугольник не существует'
    elif a == b or a == c or b == c:
        log.info('Равнобедренный')
        return 'Треугольник равнобедренный'
    else:
        log.info('Разносторонний')
        return 'Треугольник разносторонний'


print(check_triangle(args.a, args.b, args.c))
# def test_triangle():
# assert check_triangle(2, 3, 6) == 'Такой треугольник не существует', False

check_triangle(2, 2, 2)
check_triangle(1, 2, 7)