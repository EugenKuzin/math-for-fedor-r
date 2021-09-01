#!/usr/bin/env python3

def factorial(a: int) -> int:
    '''Multiply a given integer by every integer below it.'''
    if a < 0:
        print('\n\t' + 'An integer should be non-negative!' + '\n')
        try:
            a = int(input('\t\t> '))
            return factorial(a)
        except:
            print('\n\t' + 'Enter an integer!' + '\n')
            a = int(input('\t\t> '))
            return factorial(a)
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
    print('\n\t' + 'RESULT: ', factorial(a), '\n')

if __name__ == '__main__':
    print('\n\t' + 'Enter a non-negative integer to perform factorial calculations:' + '\n')
    main()
