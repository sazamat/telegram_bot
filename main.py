import telebot
from telebot import types

bot = telebot.TeleBot('5361103865:AAFjSghLg2SbsLi4LNfNFmUnBL5M7x-O8m4')


@bot.message_handler(commands=['start'])
def start(message):
    msg = f'Привет,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, msg, parse_mode='html')


# @bot.message_handler()
# def start(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('16178365.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я вас не понимаю', parse_mode='html')


@bot.message_handler(content_types='photo')
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Уау крутое фото!', parse_mode='html ')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)


bot.polling(none_stop=True)
