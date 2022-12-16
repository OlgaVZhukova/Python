# Реализуйте алгоритм перемешивания списка.

import random


list_num = []
for i in range(10):
    a = random.randint(1, 10)
    list_num.append(a)

print(list_num)
random.shuffle(list_num)
print(list_num)
