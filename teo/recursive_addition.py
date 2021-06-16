def successor(x):
    return x + 1

def predecessor(x):
    return x - 1

def sum(a, b):
    return a if b == 0 else successor(sum(a, predecessor(b)))

a = int(input())
b = int(input())

print(sum(a, b))
