from credentials import *
from init import *
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

tech_buzzwords = ["ar", "vr", "blockchain", "crypto", \
        "machine learning", "cloud", "HD"]

def find_buzzword(bot, update):
    words = update.message.text.split()
    for message_word in words:
        for buzzword in tech_buzzwords:
            if buzzword in message_word:
                bot.send_message(chat_id=update.message.chat_id, \
                    text="AR VR BLOCKCHAIN CRYTO CLOUD MACHINE LEARNING HHHHHHHHHD PORRRRNNNNNN!!!!!")
                return

bot = get_bot()
updater = Updater(token=get_api_key())
dispatcher = updater.dispatcher
echo_handler = MessageHandler((Filters.group | Filters.text), find_buzzword)
dispatcher.add_handler(echo_handler)
updater.start_polling()
