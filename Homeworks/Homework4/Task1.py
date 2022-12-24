# Вычислить число c заданной точностью d.
# Пример:
# при d = 0.001, π = 3.141.


import math

d = str(input("Введите точность числа 'π' (например 0,001): "))
length = len(d.split('.,')[-1])
print(f'π = {str(math.pi)[:length]}')

