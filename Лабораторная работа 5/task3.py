def get_unique_list_numbers() -> list[int]:

    from random import randint
    rand_int_list = []

    while len(rand_int_list) != 15:
        random_number = randint(-10, 10)
        if random_number not in rand_int_list:
            rand_int_list.append(random_number)

    return rand_int_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
