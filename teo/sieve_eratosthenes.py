#!/usr/bin/env python3

from math import sqrt

def sieve(x):
    '''Print all prime numbers less than or equal to a given positive integer using Sieve of Eratosthenes.'''
    if x < 1:
        return 'An integer should be positive!'
    elif x == 1:
        return []
    else:
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
        print(x)
        return result

def main():
    print('Enter a positive integer:')
    print(sieve(int(input())))

if __name__ == '__main__':
    main()
        
