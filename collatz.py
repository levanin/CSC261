n = 22


def cycle_length(a, x = 0):
    x += 1
    if (a == 1):
        return x
    elif (a%2 == 0):
        a /= 2
    else:
        a = 3*a + 1
    return cycle_length(a, x)


print(cycle_length(n))