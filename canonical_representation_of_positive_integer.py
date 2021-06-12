from collections import Iterable # для определения функции flatten()
from sys import argv # для передачи аргументов скрипту прямо в командной строке

def flatten(lis): # рекурсивным методом делает из вложенных списков одноуровневый список
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:
             yield item

def can_repr(x):
    '''Функция раскладывает число на простые множители, которые выводит в виде кортежа.'''
    multipliers = []
    if x <= 0:
        print('Введи положительное число:')
        x = int(input('>>> '))
    if x == 1:
        return 'Единица не является простым числом'
    else:
        for i in range (x - 1, 0, -1):
            if x % i == 0:
                multipliers.append(x // i)
                temp = i
                break
        if temp == 1:
            return tuple(list(flatten(multipliers)))
        else:
            multipliers.append(can_repr(temp))
            return tuple(list(flatten(multipliers)))

script, number = argv # берем все содержимое argv, распаковываем его и назначаем в качестве значений переменных по порядку слева

print(can_repr(int(number))) # передаем аргумент функции
