def get_api_key():
    api_key = '<your api key here>'
    with open('secret/api-token.txt', 'r') as myfile:
        api_key = myfile.read().replace('\n', '')
    return api_key

def get_user_id():
    user_id = '<your user id here>'
    with open('secret/my_id.txt', 'r') as myfile:
        user_id = myfile.read().replace('\n', '')
    return user_id
