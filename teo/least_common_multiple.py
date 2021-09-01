#!/usr/bin/env python3

def lcm(a, b: int) -> int:
    '''Take two non-zero integers and return the least common multiple.'''
    if a == 0 or b == 0:
        try:
            print('\n\t' + 'Enter two non-zero integers!' + '\n')
            a = int(input('\t\t> '))
            b = int(input('\t\t> '))
            return lcm(a, b)
        except:
            print('\n\t' + 'Enter two non-zero integers!' + '\n')
            a = int(input('\t\t> '))
            b = int(input('\t\t> '))
            return lcm(a, b)
    if a < b:
        a, b = b, a
    result = a
    while result % b != 0:
        result += a
    else:
        return result

def main():
    try:
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter two non-zero integers!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', lcm(a, b), '\n')

if __name__ == '__main__':
    print('\n\t' + 'Enter two non-zero integers to find the least common multiple of those:' + '\n')
    main()
