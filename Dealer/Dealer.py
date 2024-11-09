import random as r
import os
import telebot


bot = telebot.TeleBot("7633189148:AAEDx7ju4W246D606vHGbzxmKVp8_itxAs0")
start_sticker='CAACAgIAAxkBAAEvQ2JnL3HhogPi-3AnDr0JB4OXNyofJgACCFgAAvxEeElhyXxa4pbb3jYE'
phone_sticker='CAACAgIAAxkBAAMEZy9uSrWgNot1jTeveEKLYEKTHWgAAtpoAAKOWlFJ9hd40ny0f2U2BA'

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_sticker(message.chat.id, sticker=start_sticker, message_thread_id=message.message_thread_id, reply_to_message_id=message.id)

@bot.message_handler(content_types=['sticker'])
def ale(message):
    #variants=["Холостой", "Боевой"]
    #shots=["Первый", "Второй", "Третий", "Четвертый", "Пятый", "Шестой"]
    variants=["Blank", "Live round"]
    shots=["How unfortunate", "Third", "Fourth", "Fifth", "Sixth"]
    choosed_shot=shots[r.randint(0, 4)]
    if choosed_shot==shots[0]:
        text=choosed_shot
    else:
        text = choosed_shot+" shell. "+variants[r.randint(0, 1)]
    if message.sticker.file_id==phone_sticker:
        bot.reply_to(message, text)
    print()
        
while True:
  bot.polling(non_stop = True)