def can_repr(number):

    '''Take a positive integer greater than 1 as an argument
       and return canonical representation as a list of prime numbers in ascending order.'''

    message_is_not_positive = "Введите положительное число!"
    message_one_has_no_divisors = "Единица не имеет простых множителей!"

    if number < 1:

        print(message_is_not_positive)
        return ""

    elif number == 1:

        print(message_one_has_no_divisors)
        return []

    else:

        possible_divisors = [2] + [i for i in range(3, int(number ** 0.5) + 1, 2)]
          # generate list of possible divisors not greater than the square root of the number,
          # e.g., 100 —> [2, 3, 5, 7, 9]
          # (11*11 is greater than 100)
          
        for divisor in possible_divisors:
            if number == divisor:
                return [divisor]
            if number % divisor == 0:
                return ([divisor] + can_repr(int(number / divisor)))

        return [number]


# CONSOLE LOG

n = int(input("Введите число: "))
result = can_repr(n)

print(result)

if n > 1:
    mult = 1
    for elem in result:
        mult *= elem
    print("Проверка:", mult)
