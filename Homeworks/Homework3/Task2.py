# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random


length_list = int(input('Введите сколько чисел должно быть в списке: '))
list_num = []
multiplied = []
for _ in range(length_list):
    a = random.randint(1, 10)
    list_num.append(a)
print(list_num)


if length_list % 2 == 0:
    for i in range(int(length_list / 2)):
        multiplied.append(list_num[i] * list_num[-i - 1])
else:
    for i in range(int(length_list / 2 + 1)):
        multiplied.append(list_num[i] * list_num[-i - 1])

print(f'Произведение пар чисел списка -> {multiplied}')
