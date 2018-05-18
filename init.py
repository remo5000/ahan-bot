import telegram
from credentials import *

def get_bot():
    bot = telegram.Bot(token=api_key)
    return bot

def test_bot():
    get_bot().send_message(chat_id=user_id, text='YEEHEEE boizzz!')
