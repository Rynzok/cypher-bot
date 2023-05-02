from dictionary import ATBACH, TarabL


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
