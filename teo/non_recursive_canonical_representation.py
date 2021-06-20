def can_repr(x):
    result = []
    if x <= 0:
        return []
    if x == 1:
        return []
    for i in range(x - 1, 1, -1):
        if x % i == 0:
            result += [x // i]
            x = i
    result += [x]
    return result

# print(can_repr(int(input())))
