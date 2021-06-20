def gcd(a, b):
    if a < b:
        a, b = b, a
    result = a
    while result % b != 0:
        result += result
    else:
        return result

a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))

print(gcd(a, b))
