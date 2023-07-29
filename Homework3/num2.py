# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)


text = "The first mission, Polaris Dawn, is targeted to launch no earlier than the fourth quarter of 2022 from historic Launch Complex 39A at NASA’s Kennedy Space Center in Florida. This Dragon mission will take advantage of Falcon 9 and Dragon’s maximum performance, flying higher than any Dragon mission to date and endeavoring to reach the highest Earth orbit ever flown. Dragon and the Polaris Dawn crew will spend up to five days in orbit, during which the crew will attempt the first-ever commercial spacewalk, conduct scientific research designed to advance both human health on Earth and our understanding of human health during future long-duration spaceflights, and be the first crew to test Starlink laser-based communications in space, providing valuable data for future space communications systems necessary for missions to the Moon, Mars, and beyond."

text = text.translate(str.maketrans({'.': '', ',': ''})).lower().split()
print(f'Длина текста составляет {len(text)} слов.')
frequent_words = {x: text.count(x) for x in text}
words = []
frequence = []

for key, value in frequent_words.items():
    words.append(key)
    frequence.append(value)

frequent_words = {}

for _ in range(10):
    max_frequence_index = frequence.index(max(frequence))
    frequent_words[words[max_frequence_index]] = max(frequence)
    words.pop(max_frequence_index)
    frequence.pop(max_frequence_index)

print(f'10 самых часто встречающихся слов: ')
for key, value in frequent_words.items():
    print(f'Слово "{key}" - частота повторений - {value}')