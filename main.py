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



bot = telebot.TeleBot('6224570536:AAFi5BRh9OUwi3CwJqxSg5TObeOSbBNf3DE')

stroka = ""


# Начало работы. Две кнопки выбора. Реализованно пока только шифрование
@bot.message_handler(commands=['start'])
def start(message):
    murkup = murkup_creation(button_names=['Шифрование', 'Дешифрование'])
    msg = bot.send_message(message.chat.id, 'Что ты хочешь?', reply_markup=murkup)
    bot.register_next_step_handler(msg, user_answer)


# Анализ ответа пользователя с дальнейшим переходам в другой блок.
def user_answer(message):
    if message.text == 'Шифрование' or message.text == 'назад':
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
    murkup = types.ReplyKeyboardRemove()
    if message.text == 'Вертикальная':
        msg = bot.send_message(message.chat.id, 'Введите фразу или документ', reply_markup=murkup)
        bot.register_next_step_handler(msg, vertical_shifr)
    elif message.text == 'Меандровая':
        msg = bot.send_message(message.chat.id, 'Введите фразу или документ', reply_markup=murkup)
        bot.register_next_step_handler(msg, meandr_shifr)
    elif message.text == 'Спиральная':
        msg = bot.send_message(message.chat.id, 'Введите фразу или документ', reply_markup=murkup)
        bot.register_next_step_handler(msg, spiral_shifr)
    elif message.text == 'По числовому ключу':
        msg = bot.send_message(message.chat.id, 'Введите фразу или документ', reply_markup=murkup)
        bot.register_next_step_handler(msg, numeric_key_shifr)
    elif message.text == 'Назад':
        shifrovanie_choose(message)


# Осущесвтление вертикального шифрования и создание последующего выбора
def vertical_shifr(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])

    if message.document:
        bot.send_message(message.chat.id, 'Это документ')
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'documents/' + message.document.file_name
        with open(src, 'wb+') as new_file:
            new_file.write(downloaded_file)
        message_no_space = getting_text_from_a_document(src).replace(" ", "")
        full_massiv = vertical_shifr_algoritm(message_no_space)
        global stroka
        stroka = "".join(full_massiv)
        writing_text_to_a_document(src, stroka)
        msg = bot.send_document(message.chat.id, document=open(src, 'rb'), reply_markup=murkup)
    else:
        message_no_space = message.text.replace(" ", "")
        full_massiv = vertical_shifr_algoritm(message_no_space)
        # global stroka
        stroka = "".join(full_massiv)
        msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_vert)


# Обработчик выбора пользователя после вертикального шифрования
def processing_result_shifr_vert(message):
    if message.text == 'Новая фраза':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, vertical_shifr)
    elif message.text == 'Дешифровать':
        vertical_deshifr(message)
    elif message.text == 'Назад':
        shifrovanie_choose2(message)
    elif message.text == 'В начало':
        start(message)
    else:
        bot.send_message(message.chat.id, 'Неверно. Давайте попробуем заново')
        start(message)


# Реализация вертикального дешифрования
def vertical_deshifr(message):
    global stroka
    full_massiv = vertical_deshifr_algoritm(stroka)
    stroka = "".join(full_massiv)
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_vert)


# Реализация меандрового шифрования
def meandr_shifr(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])

    if message.document:
        bot.send_message(message.chat.id, 'Это документ')
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'documents/' + message.document.file_name
        with open(src, 'wb+') as new_file:
            new_file.write(downloaded_file)
        message_no_space = getting_text_from_a_document(src).replace(" ", "")

        full_massiv = meandr_shifr_algoritm(message_no_space)
        global stroka
        stroka = "".join(full_massiv)
        writing_text_to_a_document(src, stroka)
        msg = bot.send_document(message.chat.id, document=open(src, 'rb'), reply_markup=murkup)
    else:
        message_no_space = message.text.replace(" ", "")
        full_massiv = meandr_shifr_algoritm(message_no_space)
        stroka = "".join(full_massiv)
        msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_meandr)


# Реализация меандрового дешифрования
def meandr_deshifr(message):
    global stroka
    full_massiv = meandr_deshifr_algoritm(stroka)
    stroka = "".join(full_massiv)
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_meandr)


# Обработчик выбора пользователя после меандрового шифрования
def processing_result_shifr_meandr(message):
    if message.text == 'Новая фраза':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, meandr_shifr)
    elif message.text == 'Дешифровать':
        meandr_deshifr(message)
    elif message.text == 'Назад':
        shifrovanie_choose2(message)
    elif message.text == 'В начало':
        start(message)
    else:
        bot.send_message(message.chat.id, 'Неверно. Давайте попробуем заново')
        start(message)


def spiral_shifr(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])

    if message.document:
        bot.send_message(message.chat.id, 'Это документ')
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'documents/' + message.document.file_name
        with open(src, 'wb+') as new_file:
            new_file.write(downloaded_file)
        message_no_space = getting_text_from_a_document(src).replace(" ", "")
        full_massiv = spiral_shifr_algoritm(message_no_space)
        global stroka
        stroka = "".join(full_massiv)
        writing_text_to_a_document(src, stroka)
        msg = bot.send_document(message.chat.id, document=open(src, 'rb'), reply_markup=murkup)
    else:
        message_no_space = message.text.replace(" ", "")
        full_massiv = spiral_shifr_algoritm(message_no_space)
        stroka = "".join(full_massiv)
        msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_spiral)


def spiral_deshifr(message):
    global stroka
    full_massiv = spiral_deshifr_algoritm(stroka)
    stroka = "".join(full_massiv)
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_spiral)


# Обработчик выбора пользователя после меандрового шифрования
def processing_result_shifr_spiral(message):
    if message.text == 'Новая фраза':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, spiral_shifr)
    elif message.text == 'Дешифровать':
        spiral_deshifr(message)
    elif message.text == 'Назад':
        shifrovanie_choose2(message)
    elif message.text == 'В начало':
        start(message)
    else:
        bot.send_message(message.chat.id, 'Неверно. Давайте попробуем заново')
        start(message)


def numeric_key_shifr(message):
    murkup = types.ReplyKeyboardRemove()
    if message.document:
        bot.send_message(message.chat.id, 'Это документ')
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'documents/' + message.document.file_name
        with open(src, 'wb+') as new_file:
            new_file.write(downloaded_file)
        global stroka
        stroka = getting_text_from_a_document(src).replace(" ", "")
        lenght = int(len(stroka))
        size = find_all_dels(lenght)
        msg = bot.send_message(message.chat.id, f'Введите последовательность из {size[0]} НЕ повторяющихся числел',
                               reply_markup=murkup)
    else:
        stroka = message.text.replace(" ", "")
        lenght = int(len(stroka))
        size = find_all_dels(lenght)
        msg = bot.send_message(message.chat.id, f'Введите последовательность из {size[0]} НЕ повторяющихся числел',
                               reply_markup=murkup)
    bot.register_next_step_handler(msg, numeric_key_shifr_step_2)


def numeric_key_shifr_step_2(message):
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    numeric_key = message.text
    global stroka
    full_massiv = numeric_key_shifr_algoritm(stroka, numeric_key)
    stroka = "".join(full_massiv)
    stroka = stroka.replace("[", "")
    stroka = stroka.replace("]", "")
    stroka = stroka.replace("'", "")
    msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_numeric_key)


def numeric_key_deshifr(message):
    global stroka
    full_massiv = numeric_key_deshifr_algoritm(stroka)
    stroka = "".join(full_massiv)
    stroka = stroka.replace("[", "")
    stroka = stroka.replace("]", "")
    stroka = stroka.replace("'", "")
    murkup = murkup_creation(button_names=['Новая фраза', 'Дешифровать', 'Назад', 'В начало'])
    msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_numeric_key)


def processing_result_shifr_numeric_key(message):
    if message.text == 'Новая фраза':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, numeric_key_shifr)
    elif message.text == 'Дешифровать':
        numeric_key_deshifr(message)
    elif message.text == 'Назад':
        shifrovanie_choose2(message)
    elif message.text == 'В начало':
        start(message)
    else:
        bot.send_message(message.chat.id, 'Неверно. Давайте попробуем заново')
        start(message)


def deshifrovanie_choose(message):
    pass


bot.polling(none_stop=True)
