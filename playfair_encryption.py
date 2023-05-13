import json


def playfair_encrypt_algorithm(message_no_space, v_key):
    length = int(len(message_no_space))
    message_no_space = message_no_space.lower()

    alphabet = [''] * 32
    n = 0
    for i in range(ord('а'), ord('я') + 1):
        alphabet[n] = chr(i)
        n += 1
    alphabet.insert(6, 'ё')
    alphabet.insert(33, '.')
    alphabet.insert(34, ',')
    alphabet.insert(35, '!')
    alphabet.insert(36, '?')
    alphabet.insert(37, ':')
    alphabet.insert(38, '(')
    alphabet.insert(39, ')')

    full_massiv = [''] * len(alphabet)

    for i in range(len(v_key)):
        alphabet.remove(v_key[i])

    for i in range(len(v_key)):
        full_massiv[i] = v_key[i]
    for i in range(len(v_key), len(full_massiv)):
        full_massiv[i] = alphabet[i - len(v_key)]

    matrix = [[''] * 10 for i in range(4)]
    n = 0
    for i in range(4):
        for j in range(10):
            matrix[i][j] = full_massiv[n]
            n += 1

    dict_playfair = {}
    for i in range(4):
        for j in range(10):
            dict_playfair[matrix[i][j]] = (i, j)

    with open("data_file.json", "w") as write_file:
        json.dump(dict_playfair, write_file)

    dict_playfair_reverse = {
            value: key for key, value in dict_playfair.items()
        }

    array_tuples = [tuple()] * length
    for i in range(length):
        array_tuples[i] = dict_playfair[message_no_space[i]]

    array_tuples_new = [tuple()]

    for i in range(0, length, 2):
        if i + 1 >= length:
            array_tuples.append(dict_playfair['ъ'])
            length += 1

        if array_tuples[i] == array_tuples[i + 1]:
            array_tuples[i + 1] = dict_playfair['ъ']

        if array_tuples[i][0] == array_tuples[i + 1][0] and array_tuples[i][1] != array_tuples[i + 1][1]:
            array_tuples_new.insert(i, (array_tuples[i][0], array_tuples[i][1] + 1))
            array_tuples_new.insert(i+1, (array_tuples[i + 1][0], array_tuples[i + 1][1] + 1))

        elif array_tuples[i][0] != array_tuples[i + 1][0] and array_tuples[i][1] == array_tuples[i + 1][1]:
            array_tuples_new.insert(i, (array_tuples[i][0] + 1, array_tuples[i][1]))
            array_tuples_new.insert(i+1, (array_tuples[i + 1][0] + 1, array_tuples[i + 1][1]))

        elif array_tuples[i][0] != array_tuples[i + 1][0] and array_tuples[i][1] != array_tuples[i + 1][1]:
            array_tuples_new.insert(i, (array_tuples[i+1][0], array_tuples[i][1]))
            array_tuples_new.insert(i+1, (array_tuples[i][0], array_tuples[i + 1][1]))

    for i in range(length):
        if array_tuples_new[i][0] > 3:
            array_tuples_new.insert(i, (0, array_tuples_new[i][1]))
            array_tuples_new.pop(i + 1)
        if array_tuples_new[i][1] > 9:
            array_tuples_new.insert(i, (array_tuples_new[i][0], 0))
            array_tuples_new.pop(i + 1)

    text = [''] * length

    for i in range(length):
        text[i] = dict_playfair_reverse[array_tuples_new[i]]

    return text


def playfair_decrypt_algorithm(message_no_space):
    length = int(len(message_no_space))
    f = open('data_file.json', )
    dict_playfair = json.load(f)
    for key in dict_playfair:
        dict_playfair[key] = tuple(dict_playfair[key])

    dict_playfair_reverse = {
        value: key for key, value in dict_playfair.items()
    }

    array_tuples = [tuple()] * length
    for i in range(length):
        array_tuples[i] = dict_playfair[message_no_space[i]]

    array_tuples_new = [tuple()]

    for i in range(0, length, 2):
        if array_tuples[i][0] == array_tuples[i + 1][0] and array_tuples[i][1] != array_tuples[i + 1][1]:
            array_tuples_new.insert(i, (array_tuples[i][0], array_tuples[i][1] - 1))
            array_tuples_new.insert(i + 1, (array_tuples[i + 1][0], array_tuples[i + 1][1] - 1))

        elif array_tuples[i][0] != array_tuples[i + 1][0] and array_tuples[i][1] == array_tuples[i + 1][1]:
            array_tuples_new.insert(i, (array_tuples[i][0] - 1, array_tuples[i][1]))
            array_tuples_new.insert(i + 1, (array_tuples[i + 1][0] - 1, array_tuples[i + 1][1]))

        elif array_tuples[i][0] != array_tuples[i + 1][0] and array_tuples[i][1] != array_tuples[i + 1][1]:
            array_tuples_new.insert(i, (array_tuples[i + 1][0], array_tuples[i][1]))
            array_tuples_new.insert(i + 1, (array_tuples[i][0], array_tuples[i + 1][1]))

    for i in range(length):
        if array_tuples_new[i][0] < 0:
            array_tuples_new.insert(i, (3, array_tuples_new[i][1]))
            array_tuples_new.pop(i + 1)
        if array_tuples_new[i][1] < 0:
            array_tuples_new.insert(i, (array_tuples_new[i][0], 9))
            array_tuples_new.pop(i + 1)

    text = [''] * length

    for i in range(length):
        text[i] = dict_playfair_reverse[array_tuples_new[i]]

    return text
