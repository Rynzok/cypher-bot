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
        binary_num = "".join(b_string)

        gray_code = convert_gray(binary_num)

        gray_code = int(gray_code, 10)
        gray_code = int.to_bytes(gray_code, 3, "big")
        full_massiv[i] = gray_code.decode('cp1251')
        # full_massiv[i] = str(message_no_space[i].encode('cp1251'))
    return full_massiv


def convert_gray(binary):
    binary = int(binary, 2)
    binary ^= (binary >> 1)
    return bin(binary)[2:]
