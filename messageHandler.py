from credentials import *
from init import *

import random
import re
import time

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

# Hardcoding triggers and responses.
# Tech related
tech_buzzwords = re.compile(r"\bar\b|\bvr\b|\bblockchain\b|\bcrypto\b|\bmachine learning\b|\bcloud\b|\bHD\b",
                     flags=re.IGNORECASE | re.MULTILINE)
tech_buzzwords_reply = ["AR VR BLOCKCHAIN CRYTO CLOUD MACHINE LEARNING HHHHHHHHHD PORRRRNNNNNN!!!!!"]

# Generic Ahan
triggers = re.compile(r"\bstfu\b.*\bahan\b|\bfuck\b.*\bahan\b", 
                         flags=re.IGNORECASE | re.MULTILINE)
trigger_replies = ["dohohohoooont be a fucker lah OUI", "LULZ", "fk youuuu LULZ jk luv <3", "thx bb xoxo", "BODOH LA U"]

# Food / Ameens
food_words= re.compile(r"\bsupper\b|\bameens\b|\bmacs\b|\bcheese fries\b|\bordering\b",
                     flags=re.IGNORECASE | re.MULTILINE)
food_replies = ["so ameens???", "you noe what time it is right", "save some cheese fries for me plez <333",
                "CHEEEESE FRIES", "now we HAVE to order", "fuck that, anyone wnna eat some MALA???"]

# Main Logic
def find_and_select_random(bot, update, regex, replies):
    message_content = update.message.text
    m = regex.search(message_content)
    if m:
        #time.sleep(random.randint(1, 2)) # Uncomment for input lag.
        bot.send_message(chat_id=update.message.chat_id, text=random.choice(replies))
        return m # Since m is not None or False, it is interpreted as a True.
    return False

# Calls all the different "reply" functions. To be passed to the echo_handler.
def chainwax(bot, update):
    # Create helper lambda to take in multiple combinations of triggers and replies.
    helper = lambda regex, replies: find_and_select_random(bot, update, regex, replies)
    # Prints the matched string to terminal for debugging.
    # Prints the re object if matched, else prints False
    print(helper(tech_buzzwords, tech_buzzwords_reply) or
          helper(triggers, trigger_replies) or
          helper(food_words, food_replies))

# Set up bot to start listening.
bot = get_bot()
updater = Updater(token=api_key)
dispatcher = updater.dispatcher
echo_handler = MessageHandler((Filters.text), chainwax)
dispatcher.add_handler(echo_handler)
updater.start_polling()
