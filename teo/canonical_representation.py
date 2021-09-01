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
<<<<<<< HEAD
    try:
        a = int(input('\t\t> '))
        print('\n\t' + 'RESULT: ', can_repr(a), '\n')
    except:
        print('\n\t' + 'Enter an integer!' + '\n')
        return main()
=======
    print('Enter a positive integer that you want to decompose into its prime factors:')
    a = int(input('> '))
    print('Result: ', can_repr(a))
>>>>>>> 3251368f439526638254314ec4f18934bb309dfb

if __name__ == '__main__':
    print('\n\t' + 'Enter an integer you want to decompose into its prime factors:' + '\n')
    main()
