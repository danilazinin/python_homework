# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все в
# озможные варианты комплектации рюкзака.



bucket_list = {'GPS навигатор': 150, 'Палатка': 3000, 'Спальный мешок': 500, 'Кастрюля': 2000, 'Короб Спичек': 5,
               ' спрей': 50, 'Продукты': 5000, 'Инструменты': 4000, 'Матрас': 1500,
               'Зарядные устройства': 300}

SIZE = 15000


def check_empty_space(sum_size, next_size):
    return sum_size + next_size <= SIZE


def count_rest(sum_size):
    return SIZE - sum_size


def collect_things():
    temp_2 = {(value, key) for key, value in bucket_list.items()}
    temp = sorted(temp_2, reverse=True)

    for i in range(len(temp)):
        sum_size = 0
        res_bucket = {}
        for j in range(i, len(temp)):
            if check_empty_space(sum_size, temp[j][0]):
                res_bucket.setdefault(temp[j][1], temp[j][0])
                sum_size += temp[j][0]
        if i == 0:
            print('Допустимый вариант: ')
        elif i == 1:
            print('Возможные варианты: ')
        print(res_bucket)


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


print(collect_things())