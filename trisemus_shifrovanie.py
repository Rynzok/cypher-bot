import json


def trisemus_decrypt_algorithm(message_no_space, v_key):
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

    for i in range(len(v_key)):
        alphabet.remove(v_key[i])

    full_massiv = [''] * 40

    for i in range(len(v_key)):
        full_massiv[i] = v_key[i]
    for i in range(len(v_key), len(full_massiv)):
        full_massiv[i] = alphabet[i - len(v_key)]

    dict_trisemus = {}
    for i in range(len(full_massiv)):
        dict_trisemus[full_massiv[i]] = i

    dict_trisemus_new = {
            value: key for key, value in dict_trisemus.items()
        }

    text = [''] * length
    massiv = [0] * length
    for i in range(length):
        massiv[i] = dict_trisemus[message_no_space[i]]

    with open("data_file.json", "w") as write_file:
        json.dump(dict_trisemus, write_file)

    for i in range(length):
        if massiv[i] > 29:
            massiv[i] -= 40

    for i in range(length):
        text[i] = dict_trisemus_new[massiv[i] + 10]

    return text


def trisemus_encrypt_algorithm(message_no_space):
    length = int(len(message_no_space))
    f = open('data_file.json', )
    dict_trisemus = json.load(f)

    massiv = [0] * length
    for i in range(length):
        massiv[i] = dict_trisemus[message_no_space[i]]

    for i in range(length):
        if massiv[i] < 10:
            massiv[i] += 40

    text = [''] * length
    dict_trisemus_new = {
            value: key for key, value in dict_trisemus.items()
        }
    for i in range(length):
        text[i] = dict_trisemus_new[massiv[i] - 10]

    return text
