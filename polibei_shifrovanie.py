from dictionary import Polibei, PolibeiK


def polibei_shirf_algoritm_1(message_no_space):
    lenght = int(len(message_no_space))
    massiv = [[0] * 2] * lenght
    full_massiv = [''] * lenght
    text = [''] * lenght
    for i in range(lenght):
        massiv[i] = (Polibei[message_no_space[i]])
        a = massiv[i][0] + 1
        if a == 6:
            a = 0
        b = massiv[i][1]
        full_massiv[i] = str(a) + str(b)
        text[i] = PolibeiK[full_massiv[i]]
    return text


def polibei_deshirf_algoritm_1(message_no_space):
    lenght = int(len(message_no_space))
    massiv = [[0] * 2] * lenght
    full_massiv = [''] * lenght
    text = [''] * lenght
    for i in range(lenght):
        massiv[i] = (Polibei[message_no_space[i]])
        a = massiv[i][0] - 1
        if a == -1:
            a = 5
        b = massiv[i][1]
        full_massiv[i] = str(a) + str(b)
        text[i] = PolibeiK[full_massiv[i]]
    return text


def polibei_shirf_algoritm_2(message_no_space):
    lenght = int(len(message_no_space))
    massiv = [[0] * 2] * lenght
    massiv2 = [0] * (lenght * 2)
    full_massiv = [''] * lenght
    text = [''] * lenght
    for i in range(lenght):
        massiv[i] = (Polibei[message_no_space[i]])
    n = 0
    for i in range(2):
        for j in range(lenght):
            massiv2[n] = massiv[j][i]
            n += 1
    n = 0
    for i in range(lenght):
        full_massiv[i] = str(massiv2[n]) + str(massiv2[n+1])
        text[i] = PolibeiK[full_massiv[i]]
        n += 2
    return text


def polibei_deshirf_algoritm_2(message_no_space):
    lenght = int(len(message_no_space))
    massiv = [[0] * 2] * lenght
    massiv2 = [0] * (lenght * 2)
    full_massiv = [''] * lenght
    text = [''] * lenght
    for i in range(lenght):
        massiv[i] = (Polibei[message_no_space[i]])
    n = 0
    for i in range(lenght):
        for j in range(2):
            massiv2[n] = massiv[i][j]
            n += 1
    n = 0
    for i in range(lenght):
        full_massiv[i] = str(massiv2[n]) + str(massiv2[n+lenght])
        text[i] = PolibeiK[full_massiv[i]]
        n += 1
    return text
