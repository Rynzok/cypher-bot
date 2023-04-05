from faind_dels import find_all_dels


def double_shifr_algoritm(stroka, numeric_key, array_of_numbers):
    n = 0
    size = find_all_dels(int(len(stroka)))
    dict_row = {}
    row = [''] * size[0]
    massiv = [[''] * size[0] for i in range(size[1])]

    for j in range(size[0]):
        for i in range(size[1]):
            massiv[i][j] = stroka[n]
            n += 1

    full_massiv = [''] * size[1]

    for i in range(size[1]):
        dict_row[int(numeric_key[i])] = []
        for j in range(size[0]):
            row[j] = massiv[i][j]
        line = "".join(row)
        dict_row[int(numeric_key[i])].append(line)

    for i in range(len(array_of_numbers)):
        full_massiv[i] = str(dict_row.get(array_of_numbers[i]))
    return full_massiv


def double_deshifr_algoritm(stroka, numeric_key, array_of_numbers):
    n = 0
    size = find_all_dels(int(len(stroka)))
    dict_row = {}
    row = [''] * size[0]
    massiv = [[''] * size[0] for i in range(size[1])]

    for i in range(size[1]):
        dict_row[array_of_numbers[i]] = []
        for j in range(size[0]):
            row[j] = stroka[n]
            n += 1
        line = "".join(row)
        dict_row[array_of_numbers[i]].append(line)

    for i in range(size[1]):
        line = "".join(dict_row.get(int(numeric_key[i])))
        for j in range(size[0]):
            massiv[i][j] = line[j]
    n = 0
    full_massiv = [''] * int(len(stroka))
    for j in range(size[0]):
        for i in range(size[1]):
            full_massiv[n] = str(massiv[i][j])
            n += 1

    return full_massiv
