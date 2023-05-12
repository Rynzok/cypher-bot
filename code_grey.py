def code_grey_shifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))
    full_massiv = [''] * lenght
    for i in range(lenght):
        byte_array = message_no_space[i].encode('cp1251')
        binary_int = int.from_bytes(byte_array, "big")
        binary_string = bin(binary_int)[2:]

        gray_code = convert_gray(binary_string)

        gray_code = int(gray_code, 2)
        gray_code = gray_code.to_bytes(3, "big")
        full_massiv[i] = gray_code.decode('cp1251')
    return full_massiv


def convert_gray(binary):
    binary = int(binary, 2)
    binary ^= (binary >> 1)
    return bin(binary)[2:]


def code_grey_deshifr_algoritm(message_no_space):
    lenght = int(len(message_no_space))
    full_massiv = [''] * lenght
    for i in range(lenght):
        gray_array = message_no_space[i].encode('cp1251')
        gray_int = int.from_bytes(gray_array, "big")
        gray_string = bin(gray_int)[2:]

        binary_code = convert_binary(gray_string)

        binary_code = int(binary_code, 2)
        binary_code = binary_code.to_bytes(3, "big")
        full_massiv[i] = binary_code.decode('cp1251')
    return full_massiv


def convert_binary(gray_code):
    binary = 0
    gray_code = int(gray_code, 2)
    while gray_code > 0:
        binary ^= gray_code
        gray_code >>= 1

    return bin(binary)[2:]
