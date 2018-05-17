import telegram
from credentials import *

def get_bot():
    bot = telegram.Bot(token=get_api_key())
    return bot

def test_bot():
    get_bot().send_message(chat_id=get_user_id(), text='YEEHEEE boizzz!')
