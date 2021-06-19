def factorial(a):
    if a == 0:
        return 1
    result = a * factorial(a - 1)
    return result

a = int(input())

print(factorial(a))
