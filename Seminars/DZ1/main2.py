# Напишите программу, для проверки истинности утверждения: not(XvYvZ)=notX^notY^notZ

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            print(f'{x},{y},{z}')
            if not(x or y or z) == (not x) and (not y) and (not z):
                print('Истинно')
            else:
                print('Не истинно')