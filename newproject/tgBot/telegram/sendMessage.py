import requests
from .models import TeleSetting


def sendTelegram(text):
    settings = TeleSetting.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    req = requests.post(method, data={
    'chat_id': chat_id,
    'text': text
    })