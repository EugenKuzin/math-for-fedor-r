#!/usr/bin/env python3

def factorial(a):
    if a == 0:
        return 1
    result = a * factorial(a - 1)
    return result

def main():
    a = int(input())
    print(factorial(a))

if __name__ == '__main__':
    main()
