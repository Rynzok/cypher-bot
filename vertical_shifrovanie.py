import math


def vertical_shifr_algoritm(message_no_space):

    lenght = int(len(message_no_space))
    n = 0
    size = int(math.ceil(lenght/2))
    massiv = [[0 for i in range(2)] for j in range(size)]

    for i in range(size):
        for j in range(2):
            massiv[i][j] = message_no_space[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break
    full_massiv = [''] * lenght
    n = 0

    for j in range(2):
        for i in range(size):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1

    return full_massiv


def vertical_deshifr_algoritm(stroka):
    lenght = int(len(stroka))
    n = 0
    size = int(math.ceil(lenght / 2))
    massiv = [[0 for i in range(2)] for j in range(size)]

    for j in range(2):
        for i in range(size):
            massiv[i][j] = stroka[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break

    full_massiv = [''] * lenght
    n = 0

    for i in range(size):
        for j in range(2):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1

    return full_massiv
