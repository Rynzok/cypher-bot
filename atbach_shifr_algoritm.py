from dictionary import ATBACH


def atbach_shifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))

    full_massiv = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = ATBACH[message_no_space[i]]

    return full_massiv
