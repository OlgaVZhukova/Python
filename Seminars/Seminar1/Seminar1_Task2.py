# Напишите программу, которая на вход принимает 5 чисел и находит максимальное их них.

a = int(input())
max = a
for i in range(4):
	a = int(input())
	if a > max:
		max = a
print(max)
