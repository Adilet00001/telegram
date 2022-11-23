# SECONDBOT
import telebot

bot = telebot.TeleBot("5876624765:AAF_tOxIpKxcaP64QLCDJXYAyL_O5iOrFBI")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет давай поиграем, задавай мне вопросы!", parse_mode='html')


@bot.message_handler()
def name(message):
    if message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, "Меня зовут BOT", parse_mode='html')
    elif message.text == "Что делаешь?":
        bot.send_message(message.chat.id, "Работаю а ты?", parse_mode='html')
    elif message.text == "Откуда ты?":
        bot.send_message(message.chat.id, "Я из Виртуалного Мира", parse_mode='html')
    elif message.text == "image":
        image = open('img/bmw.jpeg', 'rb')
        bot.send_photo(message.chat.id, image)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop=True)