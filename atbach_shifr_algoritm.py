from dictionary import ATBACH, TarabL, DNK


def atbach_shifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))

    full_massiv = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = ATBACH[message_no_space[i]]

    return full_massiv


def tarabarckai_letter(message_no_space):
    lenght = int(len(message_no_space))

    full_massiv = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = TarabL[message_no_space[i]]

    return full_massiv


def dnk_shifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))

    full_massiv = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = DNK[message_no_space[i]]

    return full_massiv


def dnk_deshifr_algoritm(message_no_space):
    lenght = int(len(message_no_space) / 3)
    n = 0
    full_massiv = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = message_no_space[n] + message_no_space[n + 1] + message_no_space[n + 2]
        n += 3
        full_massiv[i] = DNK[full_massiv[i]]

    return full_massiv
