def add(*args):
    sum = 0
    for arg in args:
        sum += arg

    return sum


def calculate(x, y, *args, **kwargs):
    if kwargs.get('func') == 'add':
        return add(x, y)


print(calculate(2, 4, func='add'))
