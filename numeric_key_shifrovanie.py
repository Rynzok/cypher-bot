from faind_dels import find_all_dels


def numeric_key_shifr_algoritm(stroka, numeric_key):
    lenght = int(len(stroka))
    n = 0
    size = find_all_dels(lenght)
    dict_row = {}
    column = [0] * size[1]
    massiv = [[0] * size[0] for i in range(size[1])]
    array_of_numbers = [0] * len(numeric_key)

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
            dict_row[array_of_numbers[j]].append(massiv[i][j])

    for i in range(len(array_of_numbers)):
        cursor = array_of_numbers[i]
        pos = i

        while pos > 0 and array_of_numbers[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            array_of_numbers[pos] = array_of_numbers[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        array_of_numbers[pos] = cursor

    full_massiv = str([dict_row[key] for key in dict_row])
    return full_massiv
