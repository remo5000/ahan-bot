from credentials import *
from init import *
import resources as res
import re
from typing import Optional

import random

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


# Main Logic
def find_and_select_random(message: str, regex: re, replies: [str]) -> Optional[str]:
    """Tries to match a given regex with a Telegram Update, and chooses a random reply if there is a match."""
    match = regex.search(message)
    if match:
        return random.choice(replies)
    else:
        return None


def chainwax(bot, update):
    """Calls all the different "reply" functions. To be passed to the echo_handler."""
    # Create helper lambda to take in multiple combinations of triggers and replies.
    helper = lambda regex, replies: find_and_select_random(bot, update, regex, replies)
    # Prints the matched string to terminal for debugging.
    # Prints the re object if matched, else prints False
    print(helper(res.tech_buzzwords, res.tech_buzzwords_reply) or
          helper(res.triggers, res.trigger_replies) or
          helper(res.food_words, res.food_replies))

    # message_content = update.message.text
    # bot.send_message(chat_id=update.message.chat_id, text=random.choice(replies))
# Set up bot to start listening.
bot = get_bot()
updater = Updater(token=api_key)
dispatcher = updater.dispatcher
echo_handler = MessageHandler((Filters.text), chainwax)
dispatcher.add_handler(echo_handler)
updater.start_polling()
print("Ahan bot started\nYEHEEHEEHEE") # Init message.
