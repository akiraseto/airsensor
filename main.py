from time import sleep
from datetime import datetime
import sys
import sqlite3

import ht_sensor
import co2_sensor
import bmp_sensor
from line_Notify import lineNotify

def main():
    # 取得間隔(秒)
    # 第一引数に数字を与えると取得間隔になる
    cycle = 1 * 60
    arg = sys.argv
    if len(arg) > 1:
        cycle = int(arg[1])

    # lineNotifyする数値
    NOTIFY_TEMP = 35
    NOTIFY_DI = 85
    # NOTIFY_CO2 = 850
    NOTIFY_CO2 = 2000
    #lineへの通知間隔
    LINE_CYCLE = 10 * 60
    last_line = datetime(2000, 1, 1)  # 適当に初期化

    #DBへの書き込み間隔
    DB_CYCLE = 15 * 60
    last_db = datetime(2000, 1, 1)  # 適当に初期化

    htsensor = ht_sensor.DhtSensor()
    co2sensor = co2_sensor.Co2Sensor()
    bmpsensor = bmp_sensor.BmpSensor()
    print("")

    while True:
        temp_ht, humi = htsensor.run()
        co2, tvoc = co2sensor.run()
        temp, press, alti, sea = bmpsensor.run()

        now = datetime.now()
        date_time = "{0:%Y-%m-%d %H:%M:%S}".format(now)

        # co2が検出されてからスタート
        if co2 == 0:
            continue

        # 値を整える
        temp = round(temp, 2)
        humi = round(humi, 2)
        co2 = round(co2, 2)
        tvoc = round(tvoc, 2)
        press = round(press / 100, 2)
        alti = round(alti, 2)
        sea = round(sea / 100, 2)
        # 不快指数を計算
        di = round(0.81 * temp + 0.01 * humi * (0.99 * temp - 14.3) + 46.3, 2)

        message = "\n気温:{0}*C\n湿度:{1}%\n不快指数:{2}p\n二酸化炭素:{3}ppm\n空気の汚れ:{4}ppb\n気圧:{5}hPa\n海抜:{6}m\n海面気圧:{7}hPa"
        message = message.format(temp, humi, di, co2, tvoc, press,  alti, sea)

        print("+", date_time, "----", end="")
        print(message)

        # LINEに通知&CO2外れ値を除去
        if (temp > NOTIFY_TEMP or di > NOTIFY_DI or co2 > NOTIFY_CO2) and co2 < 5000 and tvoc < 2000:
            interval_line = (now - last_line).seconds
            # ○分間は通知しない
            if interval_line > LINE_CYCLE:
                lineNotify(message)
                last_line = now
        print("")

        interval_db = (now - last_db).seconds
        # ○分間隔でDB書き込み
        if interval_db > DB_CYCLE:
            # sqlite3で保存
            dbname = '/home/pi/airsensor/airsensor.db'
            con = sqlite3.connect(dbname)
            cur = con.cursor()
            data = (temp, humi, di, co2, tvoc, press, alti, sea, date_time)
            cur.execute('insert into airsensor (temp, humi, di, co2, tvoc, press, alti, sea, date) values (?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
            con.commit()
            con.close()
            last_db = now

        sleep(cycle)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding program")
        sys.exit(0)
