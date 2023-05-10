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
