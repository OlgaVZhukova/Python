# Данная задача должна ввывести n рядов, заполненных '*' определенным образом. А именно: в первом ряду должно быть n "звездочек", во втором n-1, и так далее.
# Пример:
# Введите количество рядов: 5
# *****
# ****
# ***
# **
# *

n = int(input())
for i in range(n, 0, -1):
    print("*"*i)
