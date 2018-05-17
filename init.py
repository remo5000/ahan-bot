import telegram
from credentials import *

# For testing
bot = telegram.Bot(token=get_api_key())
bot.send_message(chat_id=get_user_id(), text='YEEHEEE boizzz!')


