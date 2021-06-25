#!/usr/bin/env python3

from non_recursive_canonical_representation import can_repr # импортирую функцию can_repr из модуля non_recursive_canonical_representation

def gcd(a, b):
    if a > b: # мне нужно, чтобы первое число было меньше, так что в другом случае я меняю эти числа местами
        a, b = b, a
    a_primes = can_repr(a) # первое (меньшее) число я раскладываю на простые множители
    result = 1 # если у чисел не будет общих простых множителей, то результат останется единицей, то есть НОД для чисел 1
    for elem in a_primes: # проверяю каждый элемент на то, могу ли я поделить второе число на него без остатка
        if b % elem == 0:
            result *= elem # если могу, то умножаю результат на этот простой множитель
            b /= elem # а второе число становится результатом выполнения этого деления
    return result

def main():
    a = int(input('Введи первое число: '))
    b = int(input('Введи второе число: '))
    print(gcd(a, b))

if __name__ == '__main__':
    main()
