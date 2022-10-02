# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input('Задайте длину списка: '))
list1 = []
for i in range(n):
    list1.append(random.randint(0, 10))
print(list1)
list2 = list1[1::2]
print(list2)
sum = 0
for i in range(len(list2)):
    sum += list2[i]
print(sum)
