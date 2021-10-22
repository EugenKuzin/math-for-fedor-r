#!/usr/bin/env python3

def euclid(a, b: int) -> int:
    '''Find the greatest common divisor of given positive integers using Euclidean algorithm.'''
    def input_check():
        print('\n\t' + 'Enter two positive integers!' + '\n')
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
        return euclid(a, b)
    if a <= 0 or b <= 0:
        try:
            return input_check()
        except:
            return input_check()
    result = 0
    if a < b:
        a, b = b, a
    if a == b:
        return 1
    if a % b == 0:
        return b
    result += euclid(b, a % b)
    return result

def main():
    try:
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter two positive integers!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', euclid(a, b), '\n')

def start():
    print('\n\t' + 'Enter two positive integers to find the greatest common divisor of those:' + '\n')
    main()

if __name__ == '__main__':
    start()
