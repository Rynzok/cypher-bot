from faind_dels import find_all_dels


def meandr_shifr_algoritm(message_no_space):
    length = int(len(message_no_space))
    n = 0
    size = find_all_dels(length)
    massiv = [[0] * size[0] for i in range(size[1])]

    for i in range(size[1]):
        for j in range(size[0]):
            massiv[i][j] = message_no_space[n]
            n += 1
            if n == length:
                break
        if n == length:
            break

    full_massiv = [''] * length
    n = 0

    for j in range(size[0]):
        if j % 2 == 0:
            for i in range(size[1]):
                if massiv[i][j] != 0:
                    full_massiv[n] = str(massiv[i][j])
                    n += 1
        if j % 2 != 0:
            for i in range(size[1]-1, -1, -1):
                if massiv[i][j] != 0:
                    full_massiv[n] = str(massiv[i][j])
                    n += 1

    return full_massiv


def meandr_deshifr_algoritm(message):
    length = int(len(message))
    n = 0
    size = find_all_dels(length)
    massiv = [[0] * size[0] for i in range(size[1])]

    for j in range(size[0]):
        if j % 2 == 0:
            for i in range(size[1]):
                massiv[i][j] = message[n]
                n += 1
        else:
            for i in range(size[1]-1, -1, -1):
                massiv[i][j] = message[n]
                n += 1
                if n == length:
                    break

    full_massiv = [''] * length
    n = 0

    for i in range(size[1]):
        for j in range(size[0]):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1
    return full_massiv
