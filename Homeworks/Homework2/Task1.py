# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11

print('Введите число: ')
num = float(input())


def sum_nums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


print(f"Сумма цифр этого числа = {sum_nums(num)}")
