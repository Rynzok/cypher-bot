# from faind_dels import find_all_dels
import math


def magic_square_shifr_algoritm(message):
    # size = find_all_dels(int(len(message)))
    # s = size[0]
    lenght = int(len(message))
    s = math.ceil(lenght**0.5)
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 0
    i = s // 2
    j = 0
    while p < lenght:
        q[i][j] = message[p]
        ti = i + 1
        if ti >= s:
            ti = 0
        tj = j - 1
        if tj < 0:
            tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1
    n = 0
    full_massiv = [''] * int(len(message))
    for i in range(s):
        for j in range(s):
            if q[i][j] != 0:
                full_massiv[n] = str(q[i][j])
                n += 1
                if n == int(len(message)):
                    break
            if n == int(len(message)):
                break
        if n == int(len(message)):
            break

    return full_massiv


def magic_square_deshifr_algoritm(message):
    lenght = int(len(message))
    # size = find_all_dels(int(len(message)))
    # s = size[0]
    s = math.ceil(lenght**0.5)
    if s % 2 == 0:
        s += 1

    massiv = [[0 for j in range(s)] for i in range(s)]
    n = 0

    for i in range(s):
        for j in range(s):
            massiv[i][j] = message[n]
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break

    full_massiv = [''] * lenght

    p = 0
    i = s // 2
    j = 0
    while p < lenght:
        full_massiv[p] = str(massiv[i][j])
        massiv[i][j] = '0'
        ti = i + 1
        if ti >= s:
            ti = 0
        tj = j - 1
        if tj < 0:
            tj = s - 1
        if massiv[ti][tj] == '0':
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1

    return full_massiv
