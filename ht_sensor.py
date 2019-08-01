from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT

PIN = 4
CYCLE = 5

print("\nDHT11 Sensor start \n")

while True:
    while True:
        humi, temp = DHT.read_retry(DHT.DHT11, PIN)
        # 異常な値なら再取得
        if (humi > 90) or (temp > 50):
            print("- error:", humi, temp)
            sleep(0.1)
            continue
        break

    # 不快指数を計算
    di = 0.81 * temp + 0.01 * humi * (0.99 * temp - 14.3) + 46.3

    # 情報を表示
    print("+", datetime.now().strftime('%H:%M:%S'), "----")
    print("Temp = {0:0.2f} *C".format(temp))
    print("Humi = {0:0.2f} %".format(humi))
    print("DI = {0:0.2f} p".format(di))
    sleep(CYCLE)

