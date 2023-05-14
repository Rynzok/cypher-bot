from dictionary import simple_dictionary


def vigenera_encrypt_algorithm(message_no_space, n_key):
    length = len(message_no_space)
    message = [0] * length
    for i in range(length):
        message[i] = simple_dictionary[message_no_space[i]]

    i = 0
    while i < length:
        for j in range(len(n_key)):
            message[i] = (message[i] + int(n_key[j])) % 66
            i += 1
            if i == length:
                break

    text = [''] * length

    for i in range(length):
        text[i] = simple_dictionary[message[i]]
    print(text)
    return text


def vigenera_decrypt_algorithm(message_no_space, n_key):
    length = len(message_no_space)
    message = [0] * length
    for i in range(length):
        message[i] = simple_dictionary[message_no_space[i]]

    i = 0
    while i < length:
        for j in range(len(n_key)):
            message[i] = (message[i] - int(n_key[j]) + 66) % 66
            i += 1
            if i == length:
                break

    text = [''] * length

    for i in range(length):
        text[i] = simple_dictionary[message[i]]
    print(text)
    return text


# vigenera_encrypt_algorithm('ПапауВасисилёнвматематике', ['13', '16', '23'])
# vigenera_decrypt_algorithm('ПапауВасисилёнвматематике', ['13', '16', '23'])

