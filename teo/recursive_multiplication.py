#!/usr/bin/env python3

def sum(a, b):
    return a if b == 0 else successor(sum(a, predecessor(b)))

def successor(x):
    return x + 1

def predecessor(x):
    return x - 1

def multiplication(a,b):
    if b == 0:
        return 0
    return a if b == 1 else sum(a, multiplication(a, predecessor(b)))

def main():
    a = int(input())
    b = int(input())
    print(multiplication(a,b))

if __name__ == '__main__':
    main()
