from random import randint


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    rand_int_list = []
    if size > (stop - start):
        raise ValueError('Размер списка должен быть меньше диапазона чисел.')

    while len(rand_int_list) != size:
        random_number = randint(start, stop)
        if random_number not in rand_int_list:
            rand_int_list.append(random_number)

    return rand_int_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))