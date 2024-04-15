strings = input().split(',')

numbers = [int(string) for string in strings]

even = [n for n in numbers if n % 2 == 0]

print(even)