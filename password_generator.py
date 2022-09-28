import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_+")


def generate_password():
    password_length = 32

    random.shuffle(characters)
    password = []

    for n in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    return password