# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
#  [2, 3, 4, 5, 6] => [12, 15, 16];
#  [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Задайте длину списка: '))
list1 = []
for i in range(n):
    list1.append(random.randint(0, 10))
print(list1)
res = 1
for i in range(int(n/2 + n % 2)):
    res = list1[i]*list1[len(list1) - i - 1]
    print(res, end=' ')
print()
