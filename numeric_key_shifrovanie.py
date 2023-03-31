from faind_dels import find_all_dels


def numeric_key_shifr_algoritm(stroka, numeric_key, array_of_numbers):
    n = 0
    size = find_all_dels(int(len(stroka)))
    dict_row = {}
    column = [0] * size[1]
    massiv = [[0] * size[0] for i in range(size[1])]

    for i in range(size[1]):
        for j in range(size[0]):
            massiv[i][j] = stroka[n]
            n += 1

    full_massiv = [''] * size[0]

    for j in range(size[0]):
        dict_row[int(numeric_key[j])] = []
        for i in range(size[1]):
            column[i] = massiv[i][j]
        line = "".join(column)
        dict_row[int(numeric_key[j])].append(line)

    for i in range(len(array_of_numbers)):
        full_massiv[i] = str(dict_row.get(array_of_numbers[i]))
    return full_massiv


def numeric_key_deshifr_algoritm(stroka, numeric_key, array_of_numbers):
    n = 0
    size = find_all_dels(int(len(stroka)))
    dict_row = {}
    column = [0] * size[1]
    massiv = [[0] * size[0] for i in range(size[1])]

    for j in range(size[0]):
        dict_row[array_of_numbers[j]] = []
        for i in range(size[1]):
            column[i] = stroka[n]
            n += 1
        line = "".join(column)
        dict_row[array_of_numbers[j]].append(line)

    for j in range(size[0]):
        full_massiv = dict_row.get(numeric_key[j])
        line = "".join(full_massiv)
        for i in range(size[1]):
            massiv[i][j] = line[i]
    n = 0
    full_massiv = [0] * int(len(stroka))
    for i in range(size[1]):
        for j in range(size[0]):
            full_massiv[n] = str(massiv[i][j])
            n += 1

    return full_massiv
