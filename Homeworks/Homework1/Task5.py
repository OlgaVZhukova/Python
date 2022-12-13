# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input('Введите координату X первой точки A: '))
y1 = int(input('Введите координату y первой точки A: '))
x2 = int(input('Введите координату X второй точки B: '))
y2 = int(input('Введите координату y второй точки B: '))

print(round(float(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))), 3))
