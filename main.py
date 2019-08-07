from time import sleep
from datetime import datetime
import sys

import ht_sensor
import co2_sensor
import bmp_sensor
from line_Notify import lineNotify


def main():
    CYCLE = 5
    last_post = datetime(2000, 1, 1)  # 適当に初期化

    # CLI引数を取得
    args = sys.argv

    htsensor = ht_sensor.DhtSensor()
    co2sensor = co2_sensor.Co2Sensor()
    bmpsensor = bmp_sensor.BmpSensor()
    print("")

    while True:
        temp_ht, humi = htsensor.run()
        co2, tvoc = co2sensor.run()
        temp_bmp, press, alti, sea = bmpsensor.run()

        # 温度を平均を取って算出
        temp = (temp_ht + temp_bmp) / 2

        # 不快指数を計算
        di = 0.81 * temp + 0.01 * humi * (0.99 * temp - 14.3) + 46.3

        print("+", datetime.now().strftime('%H:%M:%S'), "----")
        # 温度
        print("Temp = {0:0.2f} *C".format(temp))
        # ht_sensor
        print("Humi = {0:0.2f} %".format(humi))
        # 不快指数
        print("DI = {0:0.2f} p".format(di))
        # co2_sensor
        print("CO2 = {0:0.2f} ppm".format(co2))
        print("TVOC = {0:0.2f} ppb".format(tvoc))
        # bmp_sensor
        print("Pressure = {0:0.2f} hPa".format(press / 100))
        print("Altitude = {0:0.2f} m".format(alti))
        print("Sealevel Pressure = {0:0.2f} hPa".format(sea / 100))

        # LINEに通知
        message = "\n気温:{0:0.2f}*C\n湿度:{1:0.2f}%\n不快指数:{2:0.2f}p\n二酸化炭素:{3:0.2f}ppm\n空気の汚れ:{4:0.2f}ppb\n気圧:{5:0.2f}hPa\n海抜:{6:0.2f}m\n海面気圧:{7:0.2f}hPa"
        message = message.format(temp, humi, di, co2, tvoc, press / 100,  alti, sea / 100)

        if temp > 38 or di > 75 or co2 > 700:
            now = datetime.now()
            sec = (now - last_post).seconds
            # 10分は通知しない
            if sec > 10 * 60:
                lineNotify(message)
                last_post = now

        # todo:Google spread sheetにログを取る。やらないかも
        # CSVで保存（CSVが使いまわししやすい）

        # LINENotifyを引数lineで即実行。homebridgeにも使用。
        # todo:むしろ、main使わずに独立したコマンドでCSV最新からデータ取得のほうがいいか？
        if args[1] == 'line':
            lineNotify(message)
            sys.exit(0)

        print("")
        sleep(CYCLE)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding program")
        sys.exit(0)
