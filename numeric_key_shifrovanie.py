from faind_dels import find_all_dels
from work_with_json import writing_in_json
from work_with_json import reading_json


def numeric_key_shifr_algoritm(stroka, numeric_key):
    lenght = int(len(stroka))
    n = 0
    size = find_all_dels(lenght)
    dict_row = {}
    column = [0] * size[1]
    massiv = [[0] * size[0] for i in range(size[1])]
    array_of_numbers = [0] * len(numeric_key)
    writing_in_json(numeric_key, 'data.json')

    for j in range(len(numeric_key)):
        array_of_numbers[j] = int(numeric_key[j])

    for i in range(size[1]):
        for j in range(size[0]):
            massiv[i][j] = stroka[n]
            n += 1

    full_massiv = [''] * size[0]

    for j in range(size[0]):
        dict_row[array_of_numbers[j]] = []
        for i in range(size[1]):
            column[i] = massiv[i][j]
        line = "".join(column)
        dict_row[array_of_numbers[j]].append(line)

    for i in range(len(array_of_numbers)):
        cursor = array_of_numbers[i]
        pos = i

        while pos > 0 and array_of_numbers[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            array_of_numbers[pos] = array_of_numbers[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        array_of_numbers[pos] = cursor

    for i in range(len(array_of_numbers)):
        full_massiv[i] = str(dict_row.get(array_of_numbers[i]))
    return full_massiv


def numeric_key_deshifr_algoritm(stroka):
    lenght = int(len(stroka))
    numeric_key = reading_json('data.json')
    n = 0
    size = find_all_dels(lenght)
    dict_row = {}
    column = [0] * size[1]
    massiv = [[0] * size[0] for i in range(size[1])]
    array_of_numbers = [0] * len(numeric_key)
    numeric_key_right = [0] * len(numeric_key)
    for j in range(len(numeric_key)):
        array_of_numbers[j] = int(numeric_key[j])
        numeric_key_right[j] = int(numeric_key[j])
    for i in range(len(array_of_numbers)):
        cursor = array_of_numbers[i]
        pos = i

        while pos > 0 and array_of_numbers[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            array_of_numbers[pos] = array_of_numbers[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        array_of_numbers[pos] = cursor

    for j in range(size[0]):
        dict_row[array_of_numbers[j]] = []
        for i in range(size[1]):
            column[i] = stroka[n]
            n += 1
        line = "".join(column)
        dict_row[array_of_numbers[j]].append(line)

    for j in range(size[0]):
        full_massiv = dict_row.get(numeric_key_right[j])
        line = "".join(full_massiv)
        for i in range(size[1]):
            massiv[i][j] = line[i]
    n = 0
    full_massiv = [0] * lenght
    for i in range(size[1]):
        for j in range(size[0]):
            full_massiv[n] = str(massiv[i][j])
            n += 1

    return full_massiv
