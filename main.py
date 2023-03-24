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


bot = telebot.TeleBot('6224570536:AAFi5BRh9OUwi3CwJqxSg5TObeOSbBNf3DE')

stroka = ""


# Начало работы. Две кнопки выбора. Реализованно пока только шифрование
@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    shifr = types.KeyboardButton('Шифрование')
    deshifr = types.KeyboardButton('Дешифрование')
    murkup.add(shifr, deshifr)
    msg = bot.send_message(message.chat.id, 'Что ты хочешь?', reply_markup=murkup)
    bot.register_next_step_handler(msg, user_answer)


# Анализ ответа пользователя с дальнейшим переходам в другой блок.
def user_answer(message):
    if message.text == 'Шифрование' or message.text == 'назад':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        permutation = types.KeyboardButton('Перестановка')
        replacement = types.KeyboardButton('Замена')
        back = types.KeyboardButton('назад')
        murkup.add(permutation, replacement, back)
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie_choose)
    elif message.text == 'Дешифрование':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        permutation = types.KeyboardButton('Перестановка')
        replacement = types.KeyboardButton('Замена')
        back = types.KeyboardButton('назад')
        murkup.add(permutation, replacement, back)
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, deshifrovanie_choose)


# Выбранно шифрование. Выбор его типа.
def shifrovanie_choose(message):
    if message.text == 'Перестановка' or message.text == 'Назад':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        simple = types.KeyboardButton('Простая')
        hard = types.KeyboardButton('Сложная')
        back = types.KeyboardButton('назад')
        murkup.add(simple, hard, back)
        msg = bot.send_message(message.chat.id, 'Какой уровень сложности?', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie_choose2)
    elif message.text == 'Замена':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        monoalpha = types.KeyboardButton('Моноалфавитная')
        polyalpha = types.KeyboardButton('Полкалфавитная')
        back = types.KeyboardButton('Назад')
        murkup.add(monoalpha, polyalpha, back)
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, deshifrovanie_choose)
    elif message.text == 'назад':
        start(message)


# Выбор конкретного способа шифрования
def shifrovanie_choose2(message):
    if message.text == 'Простая' or message.text == 'Назад':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        vertical = types.KeyboardButton('Вертикальная')
        meandr = types.KeyboardButton('Меандровая')
        spiral = types.KeyboardButton('Спиральная')
        back = types.KeyboardButton('Назад')
        murkup.add(vertical, meandr, spiral, back)
        msg = bot.send_message(message.chat.id, 'Выбери конкретный способ шифрования', reply_markup=murkup)
        bot.register_next_step_handler(msg, shifrovanie)
    elif message.text == 'Сложная':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        monoalpha = types.KeyboardButton('Моноалфавитная')
        polyalpha = types.KeyboardButton('Полкалфавитная')
        back = types.KeyboardButton('Назад')
        murkup.add(monoalpha, polyalpha, back)
        msg = bot.send_message(message.chat.id, 'Каким способом?', reply_markup=murkup)
        bot.register_next_step_handler(msg, deshifrovanie_choose)
    elif message.text == 'назад':
        user_answer(message)


# Выбор сделан. Отправка сообщения о вводе текса для шифрования
def shifrovanie(message):
    if message.text == 'Вертикальная':
        msg = bot.send_message(message.chat.id, 'Введите фразу или документ')
        bot.register_next_step_handler(msg, vertical_shifr)
    elif message.text == 'Меандровая':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, meandr_shifr)
    elif message.text == 'Спиральная':
        msg = bot.send_message(message.chat.id, 'Введите фразу')
        bot.register_next_step_handler(msg, spiral_shifr)
    elif message.text == 'Назад':
        shifrovanie_choose(message)


# Осущесвтление вертикального шифрования и создание последующего выбора
def vertical_shifr(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    new_frase = types.KeyboardButton('Новая фраза')
    deshefrovka = types.KeyboardButton('Дешифровать')
    back = types.KeyboardButton('Назад')
    begin = types.KeyboardButton('В начало')
    murkup.add(new_frase, deshefrovka, back, begin)

    if message.document:
        # vertical_shifr_doc(message)
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
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    new_frase = types.KeyboardButton('Новая фраза')
    deshefrovka = types.KeyboardButton('Дешифровать')
    back = types.KeyboardButton('Назад')
    begin = types.KeyboardButton('В начало')
    murkup.add(new_frase, deshefrovka, back, begin)
    msg = bot.send_message(message.chat.id, f'{stroka}', reply_markup=murkup)
    bot.register_next_step_handler(msg, processing_result_shifr_vert)


# Реализация меандрового шифрования
def meandr_shifr(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    new_frase = types.KeyboardButton('Новая фраза')
    deshefrovka = types.KeyboardButton('Дешифровать')
    back = types.KeyboardButton('Назад')
    begin = types.KeyboardButton('В начало')
    murkup.add(new_frase, deshefrovka, back, begin)

    if message.document:
        # vertical_shifr_doc(message)
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
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    new_frase = types.KeyboardButton('Новая фраза')
    deshefrovka = types.KeyboardButton('Дешифровать')
    back = types.KeyboardButton('Назад')
    begin = types.KeyboardButton('В начало')
    murkup.add(new_frase, deshefrovka, back, begin)
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
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    new_frase = types.KeyboardButton('Новая фраза')
    deshefrovka = types.KeyboardButton('Дешифровать')
    back = types.KeyboardButton('Назад')
    begin = types.KeyboardButton('В начало')
    murkup.add(new_frase, deshefrovka, back, begin)

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
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    new_frase = types.KeyboardButton('Новая фраза')
    deshefrovka = types.KeyboardButton('Дешифровать')
    back = types.KeyboardButton('Назад')
    begin = types.KeyboardButton('В начало')
    murkup.add(new_frase, deshefrovka, back, begin)
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


def deshifrovanie_choose(message):
    pass


bot.polling(none_stop=True)
