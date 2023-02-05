import telebot
from config import TOKEN,keys,all_text
from extensions import CriptoConvektor,ConvertionExeption

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Здраствуйте,{message.from_user.first_name}, {all_text}, \n пример: доллар рубль 2")


@bot.message_handler(commands=["valuse"])
def values(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def conver(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConvertionExeption("Некоректное количесвто элементов")
        quote, base, amount = values
        total_base = CriptoConvektor.get_price(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message,f"Ошибка пользователя\n {e}")
    except Exception as e:
        bot.reply_to(message,f"Не удалось обработать команду")
    else:
        text = f"Цена {amount} {quote} в {base}- {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
