from dictionary import simple_dictionary


def futurama_encrypt_algorithm(message_no_space):
    length = len(message_no_space)
    full_array = [0] * length
    full_array[0] = simple_dictionary[message_no_space[0]]
    for i in range(1, length):
        full_array[i] = simple_dictionary[message_no_space[i]] + full_array[i - 1]
        if full_array[i] > 66:
            full_array[i] -= 66

    text = [''] * length

    for i in range(length):
        text[i] = simple_dictionary[full_array[i]]

    return text


def futurama_decrypt_algorithm(message_no_space):
    length = len(message_no_space)
    full_array_new = [0] * length
    full_array_new[0] = simple_dictionary[message_no_space[0]]
    for i in range(1, length):
        full_array_new[i] = simple_dictionary[message_no_space[i]] - simple_dictionary[message_no_space[i - 1]]
        if full_array_new[i] < 1:
            full_array_new[i] += 66

    text = [''] * length

    for i in range(length):
        text[i] = simple_dictionary[full_array_new[i]]

    return text
