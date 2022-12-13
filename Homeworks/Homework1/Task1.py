# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите число от 1 до 7 включительно:')
dayNumber = int(input())

def day (dayNumber):
    if dayNumber == 6 or dayNumber == 7:
        return 'Это выходной день.'
    elif dayNumber < 1 or dayNumber > 7:
        return 'Вы ввели неверное число.'
    else:
        return 'Это будний день.'

print(day(dayNumber))
