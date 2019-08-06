import config
import requests

TOKEN = config.TOKEN
API = 'https://notify-api.line.me/api/notify'

def lineNotify(message):
    # 通知をLINEに挿入
    post_data = {'message': message}
    headers = {'Authorization': 'Bearer ' + TOKEN}
    res = requests.post(API, data=post_data, headers=headers)
    print("LineNotify = " + res.text)


