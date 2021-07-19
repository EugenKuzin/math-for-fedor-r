#!/usr/bin/env python3

def successor(x):
    '''Print the next integer.'''
    return x + 1

def predecessor(x):
    '''Print the previous integer.'''
    return x - 1

def sum(a, b):
    '''Print the sum of given integers.'''
    return a if b == 0 else successor(sum(a, predecessor(b)))

def main():
    print('Enter two integers you want to sum...')
    a = int(input('> '))
    b = int(input('> '))
    print('Result:')
    print(sum(a, b))

if __name__ == '__main__':
    main()
