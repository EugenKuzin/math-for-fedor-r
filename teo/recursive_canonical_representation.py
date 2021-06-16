def can_repr(x):
    global multipliers
    if x == 1:
        return 'Единица не является простым числом'
    else:
        for i in range(x - 1, 0, -1):
            if x % i == 0:
                multipliers += [x // i]
                temp = i
                break
        if temp > 1:
            multipliers += [can_repr(temp)]
            return multipliers
        else:
            return multipliers

multipliers = []

print(can_repr(int(input())))
