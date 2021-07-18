#!/usr/bin/env python3

from canonical_representation_1 import can_repr

def gcd(a, b):
    if a > b:
        a, b = b, a
    a_primes = can_repr(a)
    result = 1
    for elem in a_primes:
        if b % elem == 0:
            result *= elem
            b /= elem
    return result

def main():
    a = int(input('Введи первое число: '))
    b = int(input('Введи второе число: '))
    print(gcd(a, b))

if __name__ == '__main__':
    main()
