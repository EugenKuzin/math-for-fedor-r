#!/usr/bin/env python3

from math import sqrt

def sieve(x: int) -> list:
    '''Print all prime numbers less than or equal to a given positive integer using Sieve of Eratosthenes.'''
    if x == 1:
        return []
    result = [2]
    not_primes = set()
    y = int(sqrt(x) // 1)
    for i in range(3, y + 1, 2):
        if i not in not_primes:
            for k in range(i ** 2, x + 1, i * 2):
                if k % i == 0:
                    not_primes.add(k)
    for i in range(3, x + 1, 2):
        if i not in not_primes:
            result.append(i)
    return result

def main():
    try:
        a = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter an integer!' + '\n')
        return main()
    if a < 1:
        print('\n\t' + 'Enter a positive integer!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', sieve(a), '\n')

def start():
    print('\n\t' + 'Enter a positive integer to find all prime numbers of those:' + '\n')
    main()

if __name__ == '__main__':
    start()
