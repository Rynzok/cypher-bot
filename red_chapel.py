

def red_chapel_cyber_algorithm(message_no_space, v_key, n_key):
    length = int(len(message_no_space))
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
    alphabet[37] = ';'
    alphabet[38] = '('
    alphabet[39] = ')'

    print(alphabet)
    # return text
    for i in range(len(v_key)):
        alphabet.remove(v_key[i])
    print(alphabet)

    dict_red_chapel = {}

    for i in range(4):
        for j in range(10):
            if i == 0:
                dict_red_chapel[v_key[j]] = str(key[i]) + str(n_key[j])
            else:
                dict_red_chapel[alphabet[j + 10*(i-1)]] = str(key[i]) + str(n_key[j])
    print(dict_red_chapel.items())


red_chapel_cyber_algorithm('папа', ['а', 'в', 'г', 'у', 'с', 'т', 'и', 'н', 'е', 'ц'], [1, 3, 4, 21, 19, 20, 10, 14, 6, 24])
