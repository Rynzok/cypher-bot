import math
from faind_dels import find_all_dels


def vertical_shifr_algoritm(message_no_space):

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

    for j in range(size[0]):
        for i in range(size[1]):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1
                if n == lenght:
                    break
            if n == lenght:
                break
        if n == lenght:
            break

    return full_massiv


def vertical_deshifr_algoritm(stroka):
    lenght = int(len(stroka))
    n = 0
    size = find_all_dels(lenght)
    massiv = [[0] * size[0] for i in range(size[1])]

    for j in range(size[0]):
        for i in range(size[1]):
            massiv[i][j] = stroka[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break

    full_massiv = [''] * lenght
    n = 0

    for i in range(size[1]):
        for j in range(size[0]):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1

    return full_massiv
