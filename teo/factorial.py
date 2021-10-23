#!/usr/bin/env python3

def factorial(a: int) -> int:
    '''Multiply a given integer by every integer below it.'''
    if a == 0:
        return 1
    result = a * factorial(a - 1)
    return result

def main():
    try:
        a = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter an integer!' + '\n')
        return main()
    if a < 0:
        print('\n\t' + 'Enter non-negative integers!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', factorial(a), '\n')

def start():
    print('\n\t' + 'Enter a non-negative integer to perform factorial calculations:' + '\n')
    main()

if __name__ == '__main__':
    start()
