# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input('Задайте длину списка: '))
list1 = []
for i in range(n):
    list1.append(round(random.uniform(1, 10), 2))
print(list1)
list2 = []
for i in list1:
    list2.append(round((i % 1), 2))
print(list2)
print(max(list2)-min(list2))
