from dictionary import simple_dictionary


def caesar_crypt_algorithm(message_no_space, step1, step2):
    lenght = int(len(message_no_space))
    full_massiv = [0] * lenght
    text = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = simple_dictionary[message_no_space[i]] * step2 + step1
        if full_massiv[i] > 66:
            while full_massiv[i] > 66:
                full_massiv[i] -= 66
        if full_massiv[i] <= 0:
            while full_massiv[i] <= 0:
                full_massiv[i] += 66
        text[i] = simple_dictionary[full_massiv[i]]
    return text


def caesar_decrypt_algorithm(message_no_space, step1, step2):
    lenght = int(len(message_no_space))
    full_massiv = [0] * lenght
    text = [''] * lenght
    for i in range(lenght):
        full_massiv[i] = simple_dictionary[message_no_space[i]]
    for i in range(lenght):
        if full_massiv[i] <= step1:
            while full_massiv[i] <= step1:
                full_massiv[i] += 66
        full_massiv[i] = (full_massiv[i] - step1) / step2
        if full_massiv[i] > 66:
            while full_massiv[i] > 66:
                full_massiv[i] -= 66
        if full_massiv[i] <= 0:
            while full_massiv[i] <= 0:
                full_massiv[i] += 66
        text[i] = simple_dictionary[full_massiv[i]]

    return text
