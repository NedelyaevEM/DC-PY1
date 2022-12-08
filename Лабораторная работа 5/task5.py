from random import sample
from string import ascii_letters, digits


def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей
    symbols = ascii_letters + digits
    return ''.join(sample(symbols, 8))


print(get_random_password())
