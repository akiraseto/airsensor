from time import sleep
from datetime import datetime
import sys

from line_Notify import lineNotify
import bmp_sensor
import ht_sensor
import co2_sensor

CYCLE = 5
last_post = datetime(2000, 1, 1) # 適当に初期化

def main():
    print("")
    while True:
        print("+", datetime.now().strftime('%H:%M:%S'), "----")

        # co2_sensor
        co2, tvoc = co2_sensor.run()
        print("CO2 = {0:0.2f} ppm".format(co2))
        print("TVOC = {0:0.2f} ppb".format(tvoc))

        # ht_sensor
        temp_ht, humi = ht_sensor.run()
        print("Temp = {0:0.2f} *C".format(temp_ht))
        print("Humi = {0:0.2f} %".format(humi))


        # bmp_sensor
        temp_bmp, press, alti, sea = bmp_sensor.run()
        print("Temp = {0:0.2f} *C".format(temp_bmp))
        print("Pressure = {0:0.2f} hPa".format(press / 100))
        print("Altitude = {0:0.2f} m".format(alti))
        print("Sealevel Pressure = {0:0.2f} hPa".format(sea / 100))


        # 不快指数を計算
        # todo:温度は2つのセンサーの平均を取る
        di = 0.81 * temp_ht + 0.01 * humi * (0.99 * temp_ht - 14.3) + 46.3
        print("DI = {0:0.2f} p".format(di))

        print("")

    # LINEに通知
        # todo:メッセージ内容をフォーマット
        # last_post = lineNotify(last_post, 'guri')
        # print(last_post)

        # todo:Google spread sheetにログを取る

        sleep(CYCLE)



# todo:コードを一つに統合する ベースプログラムを作って、機能ごとに分けたプログラムを読み込む

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Basic Example")
        sys.exit(0)

