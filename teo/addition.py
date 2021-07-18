#!/usr/bin/env python3

def successor(x):
    return x + 1

def predecessor(x):
    return x - 1

def sum(a, b):
    return a if b == 0 else successor(sum(a, predecessor(b)))

def main():
    a = int(input())
    b = int(input())
    print(sum(a, b))

if __name__ == '__main__':
    main()
