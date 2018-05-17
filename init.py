import telegram

api_key = '<your api key here>'
user_id = '<your user id here>'
with open('secret/api-token.txt', 'r') as myfile:
    api_key = myfile.read().replace('\n', '')
with open('secret/my_id.txt', 'r') as myfile:
    user_id = myfile.read().replace('\n', '')

# For testing
# bot = telegram.Bot(token=api_key)
# bot.send_message(chat_id=user_id, text='YEEHEEE boizzz!')


