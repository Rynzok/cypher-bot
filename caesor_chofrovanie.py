from dictionary import simple_dictionary


def caesar_shifr_algoritm(message_no_space, step_m):
    lenght = int(len(message_no_space))
    step = 0
    for i in range(len(step_m)):
        step += int(step_m[i]) * 10**(len(step_m) - i - 1)
    full_massiv = [0] * lenght
    text = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = simple_dictionary[message_no_space[i]] + step
        if full_massiv[i] > 66:
            while full_massiv[i] > 66:
                full_massiv[i] -= 66
        if full_massiv[i] < 0:
            while full_massiv[i] < 0:
                full_massiv[i] += 66
        text[i] = simple_dictionary[full_massiv[i]]
    return text


def caesar_deshifr_algoritm(message_no_space, step_m):
    lenght = int(len(message_no_space))
    step = 0
    for i in range(len(step_m)):
        step += int(step_m[i]) * 10**(len(step_m) - i - 1)
    full_massiv = [0] * lenght
    text = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = simple_dictionary[message_no_space[i]] - step
        if full_massiv[i] > 66:
            while full_massiv[i] > 66:
                full_massiv[i] -= 66
        if full_massiv[i] < 0:
            while full_massiv[i] < 0:
                full_massiv[i] += 66
        text[i] = simple_dictionary[full_massiv[i]]
    return text
