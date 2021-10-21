#!/usr/bin/env python3

def sum(a, b: int) -> int:
    '''Return the sum of given positive integers using recursion.'''
    return a if b == 0 else successor(sum(a, predecessor(b)))

def successor(x: int) -> int:
    '''Return the next integer.'''
    return x + 1

def predecessor(x: int) -> int:
    '''Return the previous integer.'''
    return x - 1

def multiplication(a, b: int) -> int:
    '''Return the product of given non-negative integers using recursion.'''
    if b == 0:
        return 0
    return a if b == 1 else sum(a, multiplication(a, predecessor(b)))

def main():
    try:
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter integers!' + '\n')
        return main()
    if a < 0 or b < 0:
        print('\n\t' + 'Enter non-negative integers!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', multiplication(a, b), '\n')

def start():
    print('\n\t' + 'Enter two non-negative integers to get a product of those:' + '\n')
    main()

if __name__ == '__main__':
    start()
