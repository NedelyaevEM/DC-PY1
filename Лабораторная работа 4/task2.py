def get_count_char(str_):
    lower_str = str_.lower()
    letter_dict = {}

    for letter in lower_str:
        if letter.isalpha():
            if letter in letter_dict:
                    letter_dict[letter] += 1
            else:
                    letter_dict[letter] = 1

    return letter_dict


def get_percentage_dict(dict_):
    percentage_dict = {}

    for letter, amount in dict_.items():
        percentage_dict[letter] = round(amount / sum(dict_.values()) * 100, 2)

    return percentage_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. 
    На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить
     их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

main_dict = get_count_char(main_str)

print(sum(main_dict.values()))
print(get_percentage_dict(main_dict))
