from faind_dels import find_all_dels


def spiral_shifr_algoritm(message_no_space):

    lenght = int(len(message_no_space))
    n = 0
    size = find_all_dels(lenght)
    massiv = [[0] * size[0] for i in range(size[1])]

    for i in range(size[1]):
        for j in range(size[0]):
            massiv[i][j] = message_no_space[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
    full_massiv = [''] * lenght
    n = 0
    k = 0
    while n != lenght:
        j = k
        for i in range(k, size[1] - k, 1):
            full_massiv[n] = str(massiv[i][j])
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        i = size[1] - 1 - k
        for j in range(k + 1, size[0] - k, 1):
            full_massiv[n] = str(massiv[i][j])
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        j = size[0] - 1 - k
        for i in range(size[1] - 2 - k, -1 + k, -1):
            full_massiv[n] = str(massiv[i][j])
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        i = k
        for j in range(size[0] - 2 - k, 0 + k, -1):
            full_massiv[n] = str(massiv[i][j])
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        k += 1

    return full_massiv


def spiral_deshifr_algoritm(stroka):
    lenght = int(len(stroka))
    size = find_all_dels(lenght)
    massiv = [[0] * size[0] for i in range(size[1])]
    n = 0
    k = 0
    while n != lenght:
        j = k
        for i in range(k, size[1] - k, 1):
            massiv[i][j] = stroka[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        i = size[1] - 1 - k
        for j in range(k + 1, size[0] - k, 1):
            massiv[i][j] = stroka[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        j = size[0] - 1 - k
        for i in range(size[1] - 2 - k, -1 + k, -1):
            massiv[i][j] = stroka[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        i = k
        for j in range(size[0] - 2 - k, 0 + k, -1):
            massiv[i][j] = stroka[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
        k += 1

    full_massiv = [''] * lenght
    n = 0

    for i in range(size[1]):
        for j in range(size[0]):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1

    return full_massiv
