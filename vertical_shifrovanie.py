from faind_dels import find_all_dels


def vertical_shifr_algoritm(message_no_space):

    length = int(len(message_no_space))
    size = find_all_dels(length)
    massiv = filling_array_encrypt(message_no_space, size, length)
    full_massiv = get_from_array_encrypt(massiv, size, length)

    return full_massiv


def vertical_deshifr_algoritm(stroka):

    length = int(len(stroka))
    size = find_all_dels(length)
    massiv = filling_array_decrypt(stroka, size, length)
    full_massiv = get_from_array_decrypt(massiv, size, length)

    return full_massiv


def filling_array_encrypt(message, size, length):
    massiv = [[0] * size[0] for i in range(size[1])]

    n = 0
    for i in range(size[1]):
        for j in range(size[0]):
            massiv[i][j] = message[n]
            n += 1
            if n == length:
                break
        if n == length:
            break
    return massiv


def get_from_array_encrypt(massiv, size, length):
    full_massiv = [''] * length
    n = 0

    for j in range(size[0]):
        for i in range(size[1]):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1
                if n == length:
                    break
            if n == length:
                break
        if n == length:
            break
    return full_massiv


def filling_array_decrypt(message, size, length):
    massiv = [[0] * size[0] for i in range(size[1])]
    n = 0
    for j in range(size[0]):
        for i in range(size[1]):
            massiv[i][j] = message[n]
            n += 1
            if n == length:
                break
        if n == length:
            break
    return massiv


def get_from_array_decrypt(massiv, size, length):
    full_massiv = [''] * length
    n = 0

    for i in range(size[1]):
        for j in range(size[0]):
            if massiv[i][j] != 0:
                full_massiv[n] = str(massiv[i][j])
                n += 1
    return full_massiv
