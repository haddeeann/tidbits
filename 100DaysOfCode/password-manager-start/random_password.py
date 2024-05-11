import string
import random


def generate():
    letters = list(string.ascii_letters)
    numbers = list(range(0, 10))
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''.join(map(str, password_list))
    return password
