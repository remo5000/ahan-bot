from credentials import *
from init import *

from random import randint

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
    print("fns")
    # words = [w.lower() for w in update.message.text.split()]
    print(words)
    # for message_word in words:
        # print(message_word)
    for keyword in keywords:
        print(keyword)
        if keyword in update.message.text.lower():
            print("found match, chat " + update.message.chat_id)
            bot.send_message(chat_id=update.message.chat_id, \
                text=replies[randint(0, replies.length - 1)])
            return true
    return false


# only one reply
def buzzword(bot, update):
    print("buzzword")
    return find_and_select_random(bot, update, tech_buzzwords, tech_buzzwords_reply)
    # words = update.message.text.split()
    # for message_word in words:
    #     for buzzword in tech_buzzwords:
    #         if buzzword.lower() in message_word:
    #             bot.send_message(chat_id=update.message.chat_id, \
    #                 text=tech_buzzwords_reply)
    #             return true
    # return false

def triggered(bot, update):
    print("triggered")
    return find_and_select_random(bot, update, triggers, trigger_replies)

def food(bot, update):
    print("food")
    return find_and_select_random(bot, update, food_words, food_replies)


def chainwax(bot, update):
    print("chainwax")
    return buzzword(bot, update) | triggered(bot, update) | food(bot, update)

bot = get_bot()
updater = Updater(token=api_key)
dispatcher = updater.dispatcher
echo_handler = MessageHandler((Filters.text), chainwax)
dispatcher.add_handler(echo_handler)
updater.start_polling()
