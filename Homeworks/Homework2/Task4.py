#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# N = 5: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# произведение чисел на позициях 0, 3 и 4 = -10

n = int(input('Введите число: '))
list_num = list(range(-n,n+1))
print(list_num)


with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('3\n')
    data.write('4')
data.close()


