#!/usr/bin/env python3

from canonical_representation import can_repr

def gcd(a, b: int) -> int:
    '''Find the greatest common divisor of given positive integers.'''
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
    print('Enter two positive integers:')
    a = int(input('> '))
    b = int(input('> '))
    print('Result: ', gcd(a, b))

if __name__ == '__main__':
    main()
