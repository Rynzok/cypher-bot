def red_chapel_cyber_algorithm(message_no_space, v_key, n_key):
    length = int(len(message_no_space))
    message_no_space = message_no_space.lower()
    text = [''] * length
    key = [2, 6, 3, 1]
    n_key_sort = sorted(n_key)
    for i in range(len(n_key)):
        for j in range(len(n_key)):
            if n_key_sort[i] == n_key[j]:
                n_key[j] = i

    alphabet = [''] * 40
    n = 0
    for i in range(ord('а'), ord('я') + 1):
        alphabet[n] = chr(i)
        n += 1
    alphabet[32] = '.'
    alphabet[33] = ','
    alphabet[34] = '!'
    alphabet[35] = '?'
    alphabet[36] = ':'
    alphabet[37] = 'ё'
    alphabet[38] = '('
    alphabet[39] = ')'

    for i in range(len(v_key)):
        alphabet.remove(v_key[i])

    dict_red_chapel = {}

    for i in range(len(key)):
        for j in range(len(v_key)):
            if i == 0:
                dict_red_chapel[v_key[j]] = str(key[i]) + str(n_key[j])
            else:
                dict_red_chapel[alphabet[j + 10*(i-1)]] = str(key[i]) + str(n_key[j])

    for i in range(length):
        text[i] = dict_red_chapel[message_no_space[i]]

    return text


def slice_five(stroka):
    text = ''
    for i in range(0, len(stroka) - 5, 5):
        text += stroka[i:i+5] + ' '
    return text
