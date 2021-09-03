import telebot
from bot_keyboard import get_main_keyboard, cancel_keyboard
import requests
from database import add_following_link

bot_apikey = ''
bot = telebot.TeleBot(bot_apikey)


def send_menu(user_id):
    bot.send_message(user_id, "Воспользуйся кнопками",
                        reply_markup=get_main_keyboard())

@bot.message_handler(commands=['start', 'help'])
def reaction_to_command(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Я умею отслеживать изменение цены. Воспользуйся кнопками",
                        reply_markup=get_main_keyboard())
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Help в разработке")


@bot.message_handler(content_types=['text'])
def reaction_to_text(message):
    if message.text == 'Добавить отслеживаемую страницу':
        msg = bot.send_message(message.from_user.id, 'Добавьте ссылку', 
                               reply_markup=cancel_keyboard())
        bot.register_next_step_handler(msg, add_link_answer)


def add_link_answer(message):
    user_id = message.from_user.id
    if message.text == "Отмена":
        send_menu(user_id)
        return
    url = message.text
    if link_validate(user_id, url):
        if add_following_link(url, user_id):
            bot.send_message(user_id, "Успешно сохранено")
        else:
            bot.send_message(user_id, "Ошибка сохранения")
    else:
        msg = bot.send_message(user_id, "Проверьте правильность url-адреса. Повторите ввод", 
                               reply_markup=cancel_keyboard())
        bot.register_next_step_handler(msg, add_link_answer)




def link_validate(user_id, url):
    try:
        response = requests.get(url)
        if response.ok:
            return True
        else:
            return False
        
    except:
        return False


bot.polling(none_stop=True, interval=0)