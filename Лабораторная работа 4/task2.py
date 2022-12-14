def get_count_char(str_):
    lower_str = ''.join(str_.lower().split())
    letter_dict = {}
    for letter in lower_str:
        if letter in letter_dict:
                letter_dict[letter] += 1
        elif letter in '!.,':
                continue
        else:
                letter_dict[letter] = 1

    return letter_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. 
    На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить
     их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
