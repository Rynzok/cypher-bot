import telebot
from telebot import types
from vertical_shifrovanie import vertical_shifr_algoritm, vertical_deshifr_algoritm
from meandr_shifrovanie import meandr_shifr_algoritm, meandr_deshifr_algoritm
from document_processing import getting_text_from_a_document, writing_text_to_a_document
from spiral_shifrivanie import spiral_shifr_algoritm, spiral_deshifr_algoritm
from numeric_key_shifrovanie import numeric_key_shifr_algoritm, numeric_key_deshifr_algoritm
from magic_square_shifrovanie import magic_square_shifr_algoritm, magic_square_deshifr_algoritm
from double_shifrivanie import double_shifr_algoritm, double_deshifr_algoritm
from diagonal_shifrovanie import diagonal_shifr_algoritm, diagonal_deshifr_algoritm
from atbach_shifr_algoritm import atbach_shifr_algoritm, tarabarckai_letter, dnk_shifr_algoritm, dnk_deshifr_algoritm
from code_grey import code_grey_shifr_algoritm, code_grey_deshifr_algoritm
from polibei_shifrovanie import polibei_shirf_algoritm_1, polibei_deshirf_algoritm_1, polibei_shirf_algoritm_2,\
    polibei_deshirf_algoritm_2, polibei_shirf_algoritm_3, polibei_deshirf_algoritm_3
from caesor_chofrovanie import caesar_shifr_algoritm, caesar_deshifr_algoritm
from murkup_creation import murkup_creation
from faind_dels import find_all_dels
from sortirivka import fast_sort
from dictionary import simple_dictionary


bot = telebot.TeleBot('6224570536:AAFi5BRh9OUwi3CwJqxSg5TObeOSbBNf3DE')


class MessageEncryption:
    def __init__(self, type_encrypt):
        self.typy_encrypt = type_encrypt
        self.text_or_doc = ''
        self.text = ''
        self.text_encrypted = ''
        self.rows = 0
        self.columns = 0
        self.n_key = []
        self.n_key_last = []
        self.v_key = ''
        self.n_key_ascending = []
        self.src = ''

    def get_text(self, text, type_text):
        self.text = text
        self.text_or_doc = type_text

    def get_text_encrypted(self, text_encrypted):
        self.text_encrypted = text_encrypted

    def get_sides(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def get_n_key(self, n_key):
        self.n_key = list(n_key)
        array_of_numbers = [0] * len(self.n_key)
        for j in range(len(self.n_key)):
            array_of_numbers[j] = int(self.n_key[j])
        self.n_key_ascending = fast_sort(array_of_numbers)

    def get_v_key(self, v_key):
        self.v_key = v_key
        self.n_key = [0] * len(v_key)
        for i in range(len(self.n_key)):
            self.n_key[i] = simple_dictionary[v_key[i]]
        array_of_numbers = [0] * len(self.n_key)
        for j in range(len(self.n_key)):
            array_of_numbers[j] = int(self.n_key[j])
        self.n_key_ascending = fast_sort(array_of_numbers)


message_encrypt = MessageEncryption("")


# Начало работы. Две кнопки выбора. Реализованно пока только шифрование
@bot.message_handler(commands=['start'])
def start(message):
    murkup = murkup_creation(button_names=['Шифрование', 'Дешифрование'])
    msg = bot.send_message(message.chat.id, 'Что ты хочешь?', reply_markup=murkup)
    bot.register_next_step_handler(msg, user_answer)


# Анализ ответа пользователя с дальнейшим переходам в другой блок.
def user_answer(message):
    if message.text == 'Шифрование' or message.text == 'назад' or message.text == 'Назад':
        murkup = murkup_creation(button_names=['Перестановка', 'Замена', 'назад'])
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie_choose)
    elif message.text == 'Дешифрование':
        murkup = murkup_creation(button_names=['Перестановка', 'Замена', 'назад'])
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, deshifrovanie_choose)


# Выбранно шифрование. Выбор его типа.
def shifrovanie_choose(message):
    if message.text == 'Перестановка' or message.text == 'Назад':
        murkup = murkup_creation(button_names=['Простая', 'Сложная', 'назад'])
        msg = bot.send_message(message.chat.id, 'Какой уровень сложности?', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie_choose2)
    elif message.text == 'Замена':
        murkup = murkup_creation(button_names=['Моноалфавитная', 'Полиалфавитная', 'Назад'])
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie_choose3)
    elif message.text == 'назад':
        start(message)


# Выбор конкретного способа шифрования
def shifrovanie_choose2(message):
    if message.text == 'Простая' or message.text == 'Назад':
        murkup = murkup_creation(button_names=['Вертикальная', 'Меандровая', 'Спиральная', 'Диагональная', 'Назад'])
        msg = bot.send_message(message.chat.id, 'Выбери конкретный способ шифрования', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie)
    elif message.text == 'Сложная':
        murkup = murkup_creation(button_names=['Магичсекий квадрат', 'Двойная перестановка', 'По числовому ключу',
                                               'По буквенному ключу', 'Назад'])
        msg = bot.send_message(message.chat.id, 'Выбери конкретный способ шифрования', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie)
    elif message.text == 'назад':
        user_answer(message)


# Выбор конкретного способа шифрования
def shifrovanie_choose3(message):
    if message.text == 'Моноалфавитная' or message.text == 'Назад':
        murkup = murkup_creation(button_names=['Атбаш', 'Шифр ДНК', 'Тарабарская грамота', 'Код Грея',
                                               'Квадрат полибея (м-1)', 'Квадрат полибея (м-2)',
                                               'Квадрат полибея (м-3)', 'Шифр Цезаря', 'Назад'])
        msg = bot.send_message(message.chat.id, 'Выбери конкретный способ шифрования', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie)
    elif message.text == 'Полиалфавитная':
        murkup = murkup_creation(button_names=['Футрамы', 'Вижнера', 'Назад'])
        msg = bot.send_message(message.chat.id, 'Выбери конкретный способ шифрования', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie)
    elif message.text == 'назад':
        user_answer(message)


# Выбор сделан. Отправка сообщения о вводе текса для шифрования
def shifrovanie(message):
    if message.text == 'Назад':
        shifrovanie_choose(message)
        return
    murkup = types.ReplyKeyboardRemove()
    message_encrypt.typy_encrypt = message.text
    msg = bot.send_message(message.chat.id, 'Введите фразу или документ', reply_markup=murkup)
    bot.register_next_step_handler(msg, implementation_of_encryption)


# Реализация методов шифрования
def implementation_of_encryption(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    # Блок с обработкой документа или текста
    if message.document:
        bot.send_message(message.chat.id, 'Это документ')
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        message_encrypt.src = 'documents/' + message.document.file_name
        with open(message_encrypt.src, 'wb+') as new_file:
            new_file.write(downloaded_file)
        message_encrypt.get_text(getting_text_from_a_document(message_encrypt.src).replace(" ", ""), 'Документ')
    else:
        message_encrypt.get_text(message.text.replace(" ", ""), 'Текст')

    # Блок с алгоритмами шифрования в зависимости от выбора
    if message_encrypt.typy_encrypt == 'Вертикальная':
        message_encrypt.get_text_encrypted("".join(vertical_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'Меандровая':
        message_encrypt.get_text_encrypted("".join(meandr_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'Спиральная':
        message_encrypt.get_text_encrypted("".join(spiral_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'Диагональная':
        message_encrypt.get_text_encrypted("".join(diagonal_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'По числовому ключу':
        murkup2 = types.ReplyKeyboardRemove()
        size = find_all_dels(int(len(message_encrypt.text)))
        nsg = bot.send_message(message.chat.id, f'Введите последовательность из {size[0]} НЕ повторяющихся числел',
                               reply_markup=murkup2)
        bot.register_next_step_handler(nsg, numeric_key_shifr_step_2)
        return
    elif message_encrypt.typy_encrypt == 'По буквенному ключу':
        murkup2 = types.ReplyKeyboardRemove()
        size = find_all_dels(int(len(message_encrypt.text)))
        nsg = bot.send_message(message.chat.id, f'Введите последовательность из {size[0]} НЕ одинаковых русских букв',
                               reply_markup=murkup2)
        bot.register_next_step_handler(nsg, numeric_key_shifr_step_2)
        return

    elif message_encrypt.typy_encrypt == 'Двойная перестановка':
        murkup2 = types.ReplyKeyboardRemove()
        size = find_all_dels(int(len(message_encrypt.text)))
        message_encrypt.rows = size[1]
        message_encrypt.columns = size[0]
        nsg = bot.send_message(message.chat.id, f'Введите последовательность из {size[0]} НЕ одинаковых чисел',
                               reply_markup=murkup2)
        bot.register_next_step_handler(nsg, double_shifr)
        return

    elif message_encrypt.typy_encrypt == 'Магичсекий квадрат':
        message_encrypt.get_text_encrypted("".join(magic_square_shifr_algoritm(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Атбаш':
        message_encrypt.get_text_encrypted("".join(atbach_shifr_algoritm(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Тарабарская грамота':
        message_encrypt.get_text_encrypted("".join(tarabarckai_letter(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Шифр ДНК':
        message_encrypt.get_text_encrypted("".join(dnk_shifr_algoritm(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Код Грея':
        message_encrypt.get_text_encrypted("".join(code_grey_shifr_algoritm(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Квадрат полибея (м-1)':
        message_encrypt.get_text_encrypted("".join(polibei_shirf_algoritm_1(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Квадрат полибея (м-2)':
        message_encrypt.get_text_encrypted("".join(polibei_shirf_algoritm_2(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Квадрат полибея (м-3)':
        message_encrypt.get_text_encrypted("".join(polibei_shirf_algoritm_3(message_encrypt.text)))

    elif message_encrypt.typy_encrypt == 'Шифр Цезаря':
        murkup2 = types.ReplyKeyboardRemove()
        # size = find_all_dels(int(len(message_encrypt.text)))
        # message_encrypt.rows = size[1]
        # message_encrypt.columns = size[0]
        nsg = bot.send_message(message.chat.id, f'Введите число, на которое будет производиться сдвиг',
                               reply_markup=murkup2)
        bot.register_next_step_handler(nsg, caesar_shifr)
        return

    # Блок с отправкой документа, если был изначально отправлен документ
    if message_encrypt.text_or_doc == 'Документ':
        writing_text_to_a_document(message_encrypt.src, message_encrypt.text_encrypted)
        msg = bot.send_document(message.chat.id, open(f'{message_encrypt.src}', 'rb'), reply_markup=murkup)
        bot.register_next_step_handler(msg, processing_result_encrypt)
        return

    msg = bot.send_message(message.chat.id, f'{message_encrypt.text_encrypted}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_encrypt)


# Получение ключа
def numeric_key_shifr_step_2(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    if message_encrypt.typy_encrypt == 'По буквенному ключу':
        message_encrypt.get_v_key(message.text)
    else:
        message_encrypt.get_n_key(message.text)
    full_massiv = numeric_key_shifr_algoritm(message_encrypt.text, message_encrypt.n_key,
                                             message_encrypt.n_key_ascending)
    stroka = "".join(full_massiv)
    stroka = stroka.replace("[", "")
    stroka = stroka.replace("]", "")
    stroka = stroka.replace("'", "")
    message_encrypt.text_encrypted = stroka
    if message_encrypt.text_or_doc == 'Документ':
        writing_text_to_a_document(message_encrypt.src, message_encrypt.text_encrypted)
        msg = bot.send_document(message.chat.id, open(f'{message_encrypt.src}', 'rb'), reply_markup=murkup)
        bot.register_next_step_handler(msg, processing_result_encrypt)
        return
    msg = bot.send_message(message.chat.id, f'{message_encrypt.text_encrypted}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_encrypt)


# Получение первого ключа
def double_shifr(message):
    murkup = types.ReplyKeyboardRemove()
    message_encrypt.get_n_key(message.text)
    message_encrypt.n_key_last = list(message.text)
    full_massiv = numeric_key_shifr_algoritm(message_encrypt.text, message_encrypt.n_key,
                                             message_encrypt.n_key_ascending)
    stroka = "".join(full_massiv)
    stroka = stroka.replace("[", "")
    stroka = stroka.replace("]", "")
    stroka = stroka.replace("'", "")
    message_encrypt.text = stroka
    bot.send_message(message.chat.id, f'{message_encrypt.text}')
    msg = bot.send_message(message.chat.id, f'Введите последовательность из {message_encrypt.rows} НЕ одинаковых чисел',
                           reply_markup=murkup)
    bot.register_next_step_handler(msg, double_shifr_step_2)


# Получение второго ключа
def double_shifr_step_2(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    message_encrypt.get_n_key(message.text)
    full_massiv = double_shifr_algoritm(message_encrypt.text, message_encrypt.n_key,
                                        message_encrypt.n_key_ascending)
    stroka = "".join(full_massiv)
    stroka = stroka.replace("[", "")
    stroka = stroka.replace("]", "")
    stroka = stroka.replace("'", "")
    message_encrypt.text_encrypted = stroka
    if message_encrypt.text_or_doc == 'Документ':
        writing_text_to_a_document(message_encrypt.src, message_encrypt.text_encrypted)
        msg = bot.send_document(message.chat.id, open(f'{message_encrypt.src}', 'rb'), reply_markup=murkup)
        bot.register_next_step_handler(msg, processing_result_encrypt)
        return
    msg = bot.send_message(message.chat.id, f'{message_encrypt.text_encrypted}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_encrypt)


def caesar_shifr(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    message_encrypt.get_n_key(message.text)
    full_massiv = caesar_shifr_algoritm(message_encrypt.text, message_encrypt.n_key)
    stroka = "".join(full_massiv)
    # stroka = stroka.replace("[", "")
    # stroka = stroka.replace("]", "")
    # stroka = stroka.replace("'", "")
    message_encrypt.text_encrypted = stroka
    if message_encrypt.text_or_doc == 'Документ':
        writing_text_to_a_document(message_encrypt.src, message_encrypt.text_encrypted)
        msg = bot.send_document(message.chat.id, open(f'{message_encrypt.src}', 'rb'), reply_markup=murkup)
        bot.register_next_step_handler(msg, processing_result_encrypt)
        return
    msg = bot.send_message(message.chat.id, f'{message_encrypt.text_encrypted}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_encrypt)


# Выбор действий после шифрования
def processing_result_encrypt(message):
    if message.text == 'Новая фраза':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, implementation_of_encryption)
    elif message.text == 'Дешифровать':
        decryption_implementation(message)
    elif message.text == 'Назад':
        shifrovanie_choose2(message)
    elif message.text == 'В начало':
        start(message)
    else:
        bot.send_message(message.chat.id, 'Неверно. Давайте попробуем заново')
        start(message)


def decryption_implementation(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Назад', 'В начало'])
    if message_encrypt.text_or_doc == 'Документ':
        bot.send_message(message.chat.id, 'Это документ')
        open(message_encrypt.src, 'rb+')
        message_encrypt.text_encrypted = getting_text_from_a_document(message_encrypt.src).replace(" ", "")

    if message_encrypt.typy_encrypt == 'Вертикальная':
        message_encrypt.text = "".join(vertical_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))
    elif message_encrypt.typy_encrypt == 'Меандровая':
        message_encrypt.text = "".join(meandr_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))
    elif message_encrypt.typy_encrypt == 'Спиральная':
        message_encrypt.text = "".join(spiral_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))
    elif message_encrypt.typy_encrypt == 'Диагональная':
        message_encrypt.text = "".join(diagonal_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))
    elif message_encrypt.typy_encrypt == 'По числовому ключу' or message_encrypt.typy_encrypt == 'По буквенному ключу':
        message_encrypt.text = "".join(numeric_key_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", ""),
                                                                    message_encrypt.n_key,
                                                                    message_encrypt.n_key_ascending))
    elif message_encrypt.typy_encrypt == 'Магичсекий квадрат':
        message_encrypt.text = "".join(magic_square_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Двойная перестановка':
        message_encrypt.text_encrypted = "".join(double_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ",
                                                                                                                ""),
                                                                         message_encrypt.n_key,
                                                                         message_encrypt.n_key_ascending))
        bot.send_message(message.chat.id, f'{message_encrypt.text_encrypted}')
        message_encrypt.get_n_key(message_encrypt.n_key_last)
        message_encrypt.text = "".join(numeric_key_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", ""),
                                                                    message_encrypt.n_key,
                                                                    message_encrypt.n_key_ascending))

    elif message_encrypt.typy_encrypt == 'Атбаш':
        message_encrypt.text = "".join(atbach_shifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Тарабарская грамота':
        message_encrypt.text = "".join(tarabarckai_letter(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Шифр ДНК':
        message_encrypt.text = "".join(dnk_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Код Грея':
        message_encrypt.text = "".join(code_grey_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Квадрат полибея (м-1)':
        message_encrypt.text = "".join(polibei_deshirf_algoritm_1(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Квадрат полибея (м-2)':
        message_encrypt.text = "".join(polibei_deshirf_algoritm_2(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Квадрат полибея (м-3)':
        message_encrypt.text = "".join(polibei_deshirf_algoritm_3(message_encrypt.text_encrypted.replace(" ", "")))

    elif message_encrypt.typy_encrypt == 'Шифр Цезаря':
        message_encrypt.text = "".join(caesar_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", ""),
                                                               message_encrypt.n_key))

    elif message.text == 'Назад':
        shifrovanie_choose(message)

    if message_encrypt.text_or_doc == 'Документ':
        writing_text_to_a_document(message_encrypt.src, message_encrypt.text)
        msg = bot.send_document(message.chat.id, open(f'{message_encrypt.src}', 'rb'), reply_markup=murkup)
        bot.register_next_step_handler(msg, processing_result_encrypt)
        return
    msg = bot.send_message(message.chat.id, f'{message_encrypt.text}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_encrypt)


def deshifrovanie_choose(message):
    bot.send_message(message.chat.id, 'Контент в разработке')
    start(message)


bot.polling(none_stop=True)
