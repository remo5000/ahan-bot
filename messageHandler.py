from credentials import *
from init import *
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    # text = update.message.text here because we want to retrieve the text from the original message and send the same thing back

bot = get_bot()
updater = Updater(token=get_api_key())
dispatcher = updater.dispatcher
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
