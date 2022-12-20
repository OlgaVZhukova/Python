# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


length_list = int(input('Введите сколько чисел должно быть в списке: '))
list_float_num = []
for _ in range(length_list):
    list_float_num.append(round(uniform(1, 10), 2))
print(list_float_num)


for i in range(length_list):
    list_float_num[i] = list_float_num[i] - int(list_float_num[i])
list_float_num.sort()
dif_numbers = list_float_num[-1] - list_float_num[0]
print(f'Разница между максимальным и минимальным значением дробной части элементов: {round(dif_numbers, 2)}')
