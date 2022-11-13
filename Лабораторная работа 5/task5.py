def get_random_password() -> str:

    from random import sample
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    return ''.join(sample(symbols, 8))


print(get_random_password())
