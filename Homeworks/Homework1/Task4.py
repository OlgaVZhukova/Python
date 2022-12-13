# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти: '))

if quarter_number > 4 or quarter_number < 1:
    print('Вы ввели неправильную четверть. Введите число от 1 до 4 включительно.')
elif quarter_number == 1:
    print('x > 0 и y > 0')
elif quarter_number == 2:
    print('x < 0 и y > 0')
elif quarter_number == 3:
    print('x < 0 и y < 0')
else: print('x > 0 и y < 0')
