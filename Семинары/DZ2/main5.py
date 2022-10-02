# Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

import random
lister = [13, 65, 78, 56, 5, 28, 21]
print(lister)
list1 = []
for i in range(len(lister)):
    k = random.randint(0, len(lister) - 1)
    list1.append(lister[k])  
print(list1)
