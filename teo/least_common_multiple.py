#!/usr/bin/env python3

def lcm(a, b):
    if a < b:
        a, b = b, a
    result = a
    while result % b != 0:
        result += a
    else:
        return result

def main():
    a = int(input('Введи первое число: '))
    b = int(input('Введи второе число: '))
    print(lcm(a, b))

if __name__ == '__main__':
    main()
