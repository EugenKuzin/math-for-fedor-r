#!/usr/bin/env python3

from non_recursive_canonical_representation import can_repr

def prime_nums_not_greater_than(x):
    result = []
    for i in range(2, x + 1):
        if [i] == can_repr(i):
            result.append(i)
    return result

def main():
    print(prime_nums_not_greater_than(int(input('Введи число: '))))

if __name__ == '__main__':
    main()
