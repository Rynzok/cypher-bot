from faind_dels import find_all_dels


def diagonal_shifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))
    size = find_all_dels(lenght)
    massiv = [[0] * size[0] for i in range(size[1])]
    dif = size[1] - size[0]
    n = 0
    if dif <= 1:
        p = 1
    else:
        p = 0
    k = 1
    i = 0
    j = 0
    while n != lenght:
        massiv[i][j] = message_no_space[n]
        ti = i - 1
        tj = j + 1
        if ti < 0:
            ti = i + k
            k += 1
            if k >= size[1]:
                k = size[1] - 1
            tj = 0
        if tj == size[0]:
            tj = p
            dif -= 1
            if dif < 1:
                dif = 1
            if dif <= 1:
                p += 1
            else:
                p = 0
            if p >= size[0]:
                p = size[0] - 1
            ti = size[1] - dif
        if massiv[ti][tj] != 0:
            tj = tj + 1 + (size[1] - size[0])
        i = ti
        j = tj
        n += 1

    full_massiv = [''] * lenght
    n = 0
    for i in range(size[1]):
        for j in range(size[0]):
            full_massiv[n] = str(massiv[i][j])
            n += 1
            if n == lenght:
                break
        if n == lenght:
            break

    return full_massiv


def diagonal_deshifr_algoritm(message):
    pass
