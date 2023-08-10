
# Создайте функцию генератор чисел Фибоначчи


n = int(input('Введите число: '))


def fibonacci_generator(x):
    fib1 = fib2 = 1
    for _ in range(x):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


print(list(fibonacci_generator(n)))