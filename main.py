import telebot
from telebot import types
from vertical_shifrovanie import vertical_shifr_algoritm
from vertical_shifrovanie import vertical_deshifr_algoritm
from meandr_shifrovanie import meandr_shifr_algoritm
from meandr_shifrovanie import meandr_deshifr_algoritm
from document_processing import getting_text_from_a_document
from document_processing import writing_text_to_a_document
from spiral_shifrivanie import spiral_shifr_algoritm
from spiral_shifrivanie import spiral_deshifr_algoritm
from murkup_creation import murkup_creation
from numeric_key_shifrovanie import numeric_key_shifr_algoritm
from numeric_key_shifrovanie import numeric_key_deshifr_algoritm
from faind_dels import find_all_dels
from sortirivka import fast_sort


bot = telebot.TeleBot('6224570536:AAFi5BRh9OUwi3CwJqxSg5TObeOSbBNf3DE')


class MessageEncryption:
    def __init__(self, type_encrypt):
        self.typy_encrypt = type_encrypt
        self.text_or_doc = ''
        self.text = ''
        self.text_encrypted = ''
        self.rows = 0
        self.columns = 0
        self.n_key = ''
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
        self.n_key = n_key
        array_of_numbers = [0] * len(n_key)
        for j in range(len(n_key)):
            array_of_numbers[j] = int(n_key[j])
        self.n_key_ascending = fast_sort(array_of_numbers)

    def get_v_key(self, v_key):
        self.v_key = v_key


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
        bot.register_next_step_handler(msg, deshifrovanie_choose)
    elif message.text == 'назад':
        start(message)


# Выбор конкретного способа шифрования
def shifrovanie_choose2(message):
    if message.text == 'Простая' or message.text == 'Назад':
        murkup = murkup_creation(button_names=['Вертикальная', 'Меандровая', 'Спиральная', 'По числовому ключу',
                                               'Назад'])
        msg = bot.send_message(message.chat.id, 'Выбери конкретный способ шифрования', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie)
    elif message.text == 'Сложная':
        murkup = murkup_creation(button_names=['Назад', 'Назад', 'Назад', 'Назад'])
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, deshifrovanie_choose)
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


def implementation_of_encryption(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
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

    if message_encrypt.typy_encrypt == 'Вертикальная':
        message_encrypt.get_text_encrypted("".join(vertical_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'Меандровая':
        message_encrypt.get_text_encrypted("".join(meandr_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'Спиральная':
        message_encrypt.get_text_encrypted("".join(spiral_shifr_algoritm(message_encrypt.text)))
    elif message_encrypt.typy_encrypt == 'По числовому ключу':
        murkup2 = types.ReplyKeyboardRemove()
        size = find_all_dels(int(len(message_encrypt.text)))
        nsg = bot.send_message(message.chat.id, f'Введите последовательность из {size[0]} НЕ повторяющихся числел',
                               reply_markup=murkup2)
        bot.register_next_step_handler(nsg, numeric_key_shifr_step_2)
        return
    if message_encrypt.text_or_doc == 'Документ':
        writing_text_to_a_document(message_encrypt.src, message_encrypt.text_encrypted)
        msg = bot.send_document(message.chat.id, open(f'{message_encrypt.src}', 'rb'), reply_markup=murkup)
        bot.register_next_step_handler(msg, processing_result_encrypt)
        return
    msg = bot.send_message(message.chat.id, f'Зашифровал:{message_encrypt.text_encrypted}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_encrypt)


def numeric_key_shifr_step_2(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
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
    elif message.text == 'Меандровая':
        message_encrypt.text = "".join(meandr_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))
    elif message.text == 'Спиральная':
        message_encrypt.text = "".join(spiral_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", "")))
    elif message.text == 'По числовому ключу':
        message_encrypt.text = "".join(numeric_key_deshifr_algoritm(message_encrypt.text_encrypted.replace(" ", ""),
                                                                    message_encrypt.n_key,
                                                                    message_encrypt.n_key_ascending))
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
    pass


bot.polling(none_stop=True)
