from telebot import types

def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("Добавить отслеживаемую страницу"))
    return keyboard


def cancel_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("Отмена"))
    return keyboard