#!/usr/bin/env python3

def factorial(a: int) -> int:
    '''Multiply a given positive integer by every integer below it.'''
    if a == 0:
        return 1
    result = a * factorial(a - 1)
    return result

def main():
    print('Enter a positive integer to perform factorial calculations:')
    a = int(input('> '))
    print('Result: ', factorial(a))

if __name__ == '__main__':
    main()
