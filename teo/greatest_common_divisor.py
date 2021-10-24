#!/usr/bin/env python3

from canonical_representation import can_repr

def gcd(a, b: int) -> int:
    '''Find the greatest common divisor of given positive integers.'''
    if a <= 0 or b <= 0:
        try:
            print('\n\t' + 'Enter two positive integers!' + '\n')
            a = int(input('\t\t> '))
            b = int(input('\t\t> '))
            return gcd(a, b)
        except:
            print('\n\t' + 'Enter two positive integers!' + '\n')
            a = int(input('\t\t> '))
            b = int(input('\t\t> '))
            return gcd(a, b)
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
    try:
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter integers!' + '\n')
        return main()
    if a <= 0 or b <= 0:
        print('\n\t' + 'Enter two positive integers!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', gcd(a, b), '\n')

def start():
    print('\n\t' + 'Enter two positive integers to find the greatest common divisor of those:' + '\n')
    main()

if __name__ == '__main__':
    start()
