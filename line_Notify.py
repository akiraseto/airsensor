import config
from datetime import datetime
import requests

TOKEN = config.TOKEN
API = 'https://notify-api.line.me/api/notify'

def lineNotify(last_post,message):
    # LINEに通知
    # ただし10分は通知しない
    now = datetime.now()
    sec = (now - last_post).seconds
    if sec < 10 * 60: return
    # 通知をLINEに挿入 --- (*2)
    post_data = {'message': message}
    headers = {'Authorization': 'Bearer ' + TOKEN}
    res = requests.post(API, data=post_data, headers=headers)
    print(res.text)
    return now


