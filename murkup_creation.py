from telebot import types


def murkup_creation(button_names):
    button = [0] * len(button_names)
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for i in range(len(button_names)):
        button[i] = types.KeyboardButton(f'{button_names[i]}')
        murkup.add(button[i])
    return murkup
