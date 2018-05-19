from credentials import *
from init import *

import random

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

tech_buzzwords = ["ar", "vr", "blockchain", "crypto", \
        "machine learning", "cloud", "HD"]
tech_buzzwords_reply = ["AR VR BLOCKCHAIN CRYTO CLOUD MACHINE LEARNING HHHHHHHHHD PORRRRNNNNNN!!!!!"]

triggers = ["ahan", "stfu", "stfu ahan"]
trigger_replies = ["dohohohoooont be a fucker lah OUI", "LULZ", "fk youuuu LULZ jk luv <3", "thx bb xoxo", "BODOH LA U"]

food_words = ["supper", "ameens", "macs", "cheese", "fries", "ordering"]
food_replies = ["so ameens???", "you noe what time it is right", "save some cheese fries for me plez <333", "CHEEEESE FRIES", "now we HAVE to order", "fuck that, anyone wnna eat some MALA???"]

def find_and_select_random(bot, update, keywords, replies):
    message_content = update.message.text.lower()
    if message_content in keywords:
        bot.send_message(chat_id=update.message.chat_id, text=random.choice(replies))
        return False
    return True


def buzzword(bot, update):
    print("buzzword")
    return find_and_select_random(bot, update, tech_buzzwords, tech_buzzwords_reply)

def triggered(bot, update):
    print("triggered")
    return find_and_select_random(bot, update, triggers, trigger_replies)

def food(bot, update):
    print("food")
    return find_and_select_random(bot, update, food_words, food_replies)

def chainwax(bot, update):
    print("chainwax")
    return buzzword(bot, update) and triggered(bot, update) and food(bot, update)

bot = get_bot()
updater = Updater(token=api_key)
dispatcher = updater.dispatcher
echo_handler = MessageHandler((Filters.text), chainwax)
dispatcher.add_handler(echo_handler)
updater.start_polling()
