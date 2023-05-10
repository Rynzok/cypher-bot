from dictionary import Polibei, PolibeiK


def polibei_shirf_algoritm_1(message_no_space):
    lenght = int(len(message_no_space))
    massiv = [[0] * 2] * lenght
    full_massiv = [''] * lenght
    text = [''] * lenght
    for i in range(lenght):
        massiv[i] = (Polibei[message_no_space[i]])
        if massiv[i][0] == 5:
            massiv[i][0] = -1
        full_massiv[i] = str(massiv[i][0] + 1) + str(massiv[i][1])
        text[i] = PolibeiK[full_massiv[i]]

    return text
