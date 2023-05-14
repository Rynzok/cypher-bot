def kiselev_encrypt_algoritm(message_no_space):
    length = int(len(message_no_space))
    full_massiv = [''] * length

    for i in range(length):
        full_massiv[i] = str(ord(message_no_space[i]))

    array_code = [0] * length
    for i in range(length):
        code = full_massiv[i]
        array_code[i] = int(code[1] + code[0] + code[3] + code[2])

    text = [''] * length
    for i in range(length):
        text[i] = chr(array_code[i])

    return text


def kiselev_decrypt_algoritm(message_no_space):
    length = int(len(message_no_space))
    full_massiv = [''] * length

    for i in range(length):
        full_massiv[i] = str(ord(message_no_space[i]))
    for i in range(length):
        if len(full_massiv[i]) != 4:
            full_massiv[i] = '0' + full_massiv[i]

    array_code = [0] * length
    for i in range(length):
        code = full_massiv[i]
        array_code[i] = int(code[1] + code[0] + code[3] + code[2])

    text = [''] * length
    for i in range(length):
        text[i] = chr(array_code[i])

    return text
