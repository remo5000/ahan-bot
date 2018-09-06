from credentials import *
from init import *
import resources as res

import random
import time

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


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
    print(helper(res.tech_buzzwords, res.tech_buzzwords_reply) or
          helper(res.triggers, res.trigger_replies) or
          helper(res.food_words, res.food_replies))

# Sets the global lockdown variable
def security(bot, update):
    # Only works for remo5000
    if update.message.from_user.username != "remo5000":
        return 
    message_content = update.message.text
    regex = re.compile(r"\bahan quit your shit bruv\b")
    lock = regex.search(message_content)
    regex = re.compile(r"\bahan resume pls\b")
    unlock = regex.search(message_content)
    global lockdown
    if lock:
        lockdown = True
    else if unlock:
        lockdown = False

def lockdown_wrapper(func):
   global lockdown 
   def wrapped_function(*args, **kwargs):
       if lockdown:
           return 
       else:
           return func(*args, **kwargs)

# Set up security stuff in memory
lockdown = False

# Set up bot to start listening.
bot = get_bot()
updater = Updater(token=api_key)
dispatcher = updater.dispatcher
# Handle echoes
echo_handler = MessageHandler((Filters.text), chainwax)
dispatcher.add_handler(echo_handler)
# Handle security
security_handler = MessageHandler((Filters.text), security)
dispatcher.add_handler(security_handler)
updater.start_polling()
print("Ahan bot started\nYEHEEHEEHEE") # Init message.
