import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filepath, delimiter=',', new_line='\n') -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(filepath) as f_read:
        list_of_lines = f_read.readlines()

    list_of_headers = list_of_lines[0].split(',')
    last_header = list_of_headers[-1]
    del list_of_headers[-1]
    list_of_headers.append(last_header.replace('\n', ''))

    del list_of_lines[0]

    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].replace('\n', '')

    temp_dict = {header: 0 for header in list_of_headers}
    list_of_dicts = []

    for i in range(len(list_of_lines)):
        list_of_values = [value for value in list_of_lines[i].split(',')]
        list_of_pares = []
        for j in range(len(list_of_headers)):
            pare = (list_of_headers[j], list_of_values[j])
            list_of_pares.append(pare)
        dict_ = {header: pare for (header, pare) in list_of_pares}
        list_of_dicts.append(dict_)

    return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
