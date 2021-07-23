#!/usr/bin/env python3

def can_repr(x: int) -> list:
    '''Express a given integer as the product of its prime factors.'''
    result = []
    if x <= 0:
        return []
    if x == 1:
        return []
    for i in range(x - 1, 1, -1):
        if x % i == 0:
            result += [x // i]
            x = i
    result += [x]
    return result

def main():
    print('Enter a positive integer you want to decompose into its prime factors:')
    a = int(input('> '))
    print('Result: ' + str(can_repr(a)))

if __name__ == '__main__':
    main()
