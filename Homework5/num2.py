
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

n = '/Users/Dzender/Downloads/Web разработка na Python.pdf'
print(n.rindex('/'))


def unpack_absolute_path(path: str) -> tuple:
    path_ = path[:path.rindex("/") + 1]
    filename = path[path.rindex("/") + 1:path.index('.')]
    extension = ''.join(path.split('.')[1:])
    return path_, filename, extension


print(unpack_absolute_path(n))