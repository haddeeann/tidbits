import string
from random import choice, randint, shuffle


def generate():
    letters = list(string.ascii_letters)
    numbers = list(range(0, 10))
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = ''.join(map(str, password_list))
    return password
