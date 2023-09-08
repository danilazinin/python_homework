import os
from pathlib import Path
from random import randint, random


class Serializer:
    wanted_name: str
    count_nums: int
    old_extension: str
    new_extension: str
    range_: list
    line_count: int
    filename: str

    def rename_files(self, wanted_name, count_nums, old_extension, new_extension, range_):
        start_num = 1
        for obj in os.listdir():
            if obj[-len(old_extension):] == old_extension:
                new_name = (f'{obj[range_[0]:range_[1] + 1]}{wanted_name}{start_num:0{count_nums}}'
                            f'{new_extension}')
                Path(obj).rename(new_name)
                start_num += 1

    def add_two_numbers_to_file(self, line_count, filename):
        with open(filename, 'a', encoding='utf-8') as file:
            for _ in range(line_count):
                file.write(f'{randint(-1000, 1000)} | {"{:.2f}".format(random() * 1000)}\n')


s = Serializer()