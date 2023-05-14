from dictionary import simple_dictionary


def gronsfeld_decrypt_algorithm(message_no_space, n_key):
    length = int(len(message_no_space))

    full_massiv = [0] * length
    for i in range(length):
        full_massiv[i] = message_no_space[i]
    n = 0
    while n < length:
        for i in range(len(n_key)):
            full_massiv[n] = simple_dictionary[message_no_space[n]]
            shift = full_massiv[n] + int(n_key[i])
            if shift > 66:
                shift -= 66
            full_massiv[n] = simple_dictionary[shift]
            n += 1
            if n == length:
                break

    return full_massiv


def gronsfeld_encrypt_algorithm(message_no_space, n_key):
    length = int(len(message_no_space))

    full_massiv = [0] * length
    for i in range(length):
        full_massiv[i] = message_no_space[i]
    n = 0
    while n < length:
        for i in range(len(n_key)):
            full_massiv[n] = simple_dictionary[message_no_space[n]]
            shift = full_massiv[n] - int(n_key[i])
            if shift < 1:
                shift += 66
            full_massiv[n] = simple_dictionary[shift]
            n += 1
            if n == length:
                break

    return full_massiv

