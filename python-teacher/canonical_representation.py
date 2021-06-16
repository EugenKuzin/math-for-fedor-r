num = int(input())
possible_divisors = [2] + [i for i in range(3, int(num**0.5) + 1, 2)]

def can_repr(number):
    global possible_divisors
    if number < 1:
        print("Введите положительное число!")
        return
    elif number == 1:
        print("Единица не имеет простых множителей!")
        return
    else:
        for divisor in possible_divisors:
            if number == divisor:
                return [divisor]
            if number % divisor == 0:
                return ([divisor] + can_repr(number / divisor))
        return [number]

print(can_repr(num))
