def code_grey_shifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))
    full_massiv = [''] * lenght
    for i in range(lenght):
        byte_array = message_no_space[i].encode('cp1251')
        binary_int = int.from_bytes(byte_array, "big")
        binary_string = bin(binary_int)
        b_string = [''] * (len(binary_string) - 2)
        for j in range(2, len(binary_string)):
            b_string[j - 2] = str(binary_string[j])
        full_massiv[i] = "".join(b_string)
        # full_massiv[i] = str(message_no_space[i].encode('cp1251'))
    return full_massiv
