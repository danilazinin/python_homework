# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на
# единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.



a = int(input("Введите число: "))
if a > 0 and a < 100000:
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        print(f"Число {a} простое")
    else:
        print(f"Число {a} составное")
else:
    print("Число не удовлетворяет условие")
