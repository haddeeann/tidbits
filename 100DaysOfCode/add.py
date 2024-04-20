def add(*args):
    sum = 0
    for arg in args:
        sum += arg

    return sum


print(add(1, 2, 3))
