from dictionary import simple_dictionary
import json


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


def caesar_word_crypt_algorithm(message_no_space, step1, v_key):
    lenght = int(len(message_no_space))
    message_no_space = message_no_space.lower()

    alphabet = [''] * 32
    n = 0
    for i in range(ord('а'), ord('я') + 1):
        alphabet[n] = chr(i)
        n += 1
    alphabet.insert(6, 'ё')
    alphabet_right = alphabet.copy()

    for i in range(len(v_key)):
        alphabet.remove(v_key[i])

    full_massiv = [''] * 33

    if step1 > 33:
        while step1 > 33:
            step1 -= 33

    for i in range(step1, len(v_key) + step1):
        full_massiv[i] = v_key[i - step1]
    for i in range(len(v_key) + step1, len(full_massiv)):
        full_massiv[i] = alphabet[i - (len(v_key) + step1)]
    for i in range(step1):
        full_massiv[i] = alphabet[i + len(full_massiv) - len(v_key) - step1]

    dict_caesar = {}
    for i in range(len(full_massiv)):
        dict_caesar[alphabet_right[i]] = full_massiv[i]

    text = [''] * lenght

    for i in range(lenght):
        text[i] = dict_caesar[message_no_space[i]]

    with open("data_file.json", "w") as write_file:
        json.dump(dict_caesar, write_file)

    return text


def caesar_word_decrypt_algorithm(message_no_space):
    length = int(len(message_no_space))
    f = open('data_file.json', )
    dict_caesar = json.load(f)
    text = [''] * length
    dict_caesar_new = {
            value: key for key, value in dict_caesar.items()
        }
    for i in range(length):
        text[i] = dict_caesar_new[message_no_space[i]]

    return text
