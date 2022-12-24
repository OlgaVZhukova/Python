# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: 12 -> список простых множителей: 2, 2, 3 (которые делятся на 1 и сами на себя).

prompt_number = int(input('Введите число: '))
i = 2
simple_numbers = []
while i <= prompt_number:
    if prompt_number % i == 0:
        simple_numbers.append(i)
        prompt_number //= i
    else:
        i += 1
print(f'Простые множители числа: {simple_numbers}')
