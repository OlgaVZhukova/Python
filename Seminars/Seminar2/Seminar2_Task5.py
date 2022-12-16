# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random

#создаем и заполняем список случайных чисел
list_num = [] # создадим список
for i in range(10): # заполним его случайными значениями, десятью, например
    a = random.randint(2, 5) #числа в списке будут от 2 до 5 включительно
    list_num.append(a) #добавляем в список эти случайные числа
print(list_num)

max = 0
for i in set(list_num):
    if list_num.count(i) > max:
        max = list_num.count(i)
print(max)
