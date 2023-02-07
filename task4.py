import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filepath, delimiter=',', new_line='\n') -> list[dict]:
    # TODO реализовать конвертер из csv в json

    list_of_dicts = []

    with open(filepath) as f_read:
        string_of_headers = f_read.readline().replace("\n", "")
        list_of_headers = string_of_headers.split(delimiter)

        for row in f_read:
            row = row.replace("\n", "")
            list_of_values = row.split(delimiter)
            list_of_dicts.append(dict(zip(list_of_headers, list_of_values)))

    return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
