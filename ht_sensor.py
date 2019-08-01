from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT

PIN = 4

print("\nDHT11 Sensor start \n")

for i in range(10):
    while True:
        humi, temp = DHT.read_retry(DHT.DHT11, PIN)
        # 異常な値なら再取得
        if (humi > 90) or (temp > 50):
            print("- error:", humi, temp)
            sleep(0.1)
            continue
        break
    # 情報を表示
    print("+", datetime.now().strftime('%H:%M:%S'), "----")
    print("Temp = {0:0.2f} *C".format(temp))
    print("Humi = {0:0.2f} %".format(humi))
    sleep(5)

