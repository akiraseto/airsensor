from __future__ import print_function
import qwiic_ccs811
from time import sleep
import sys
from datetime import datetime
import config

CYCLE = 5
# LINE Notifyトークン
TOKEN = config.TOKEN
API = 'https://notify-api.line.me/api/notify'
last_post = datetime(2000, 1, 1) # 適当に初期化

def runExample():
    print("\nCCS811 Sensor start \n")
    mySensor = qwiic_ccs811.QwiicCcs811()

    if mySensor.is_connected() == False:
        print("CCS811 Sensor isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    mySensor.begin()

    while True:
        mySensor.read_algorithm_results()
        print("+", datetime.now().strftime('%H:%M:%S'), "----")
        print("CO2 = {0:0.2f} ppm".format(mySensor.get_co2()))
        print("TVOC = {0:0.2f} ppb".format(mySensor.get_tvoc()))
        sleep(CYCLE)

def lineNotify(last_post):
    # LINEに通知
    # ただし10分は通知しない
    now = datetime.now()
    sec = (now - last_post).seconds
    if sec < 10 * 60: return
    # 通知をLINEに挿入 --- (*2)
    post_data = {'CO2': '50', 'TVOC': '100'}
    headers = {'Authorization': 'Bearer ' + TOKEN}
    res = requests.post(API, data=post_data,
                        headers=headers)
    print(res.text)

    # return last_post = now


if __name__ == '__main__':
    try:
        runExample()
        # lineNotify(last_post)
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Basic Example")
        sys.exit(0)

# todo:コードを一つに統合する ベースプログラムを作って、機能ごとに分けたプログラムを読み込む
