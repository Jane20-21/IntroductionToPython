# Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке
# одно число.

n = int(input('Введите число больше 0: '))
mas = []
for i in range(0, 2*n + 1):
    mas.insert(i, -n + i)
print(mas)
a = mas[2]
b = mas[5]
print(a*b)
