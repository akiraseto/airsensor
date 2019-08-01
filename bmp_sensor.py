import Adafruit_BMP.BMP085 as BMP085
from time import sleep
from datetime import datetime

CYCLE = 5

print("\nBMP180 Sensor start \n")
sensor = BMP085.BMP085()

while True:
    while True:
        temp = sensor.read_temperature()
        press = sensor.read_pressure()
        alti = sensor.read_altitude()
        sea = sensor.read_sealevel_pressure()
        # 異常な値なら再取得
        if (temp > 50) or (press > 110000) or (press < 90000) or (alti > 3776):
            print("- error:", temp, press, alti, sea)
            time.sleep(0.1)
            continue
        break

    print("+", datetime.now().strftime('%H:%M:%S'), "----")
    print("Temp = {0:0.2f} *C".format(temp))
    print("Pressure = {0:0.2f} hPa".format(press / 100))
    print("Altitude = {0:0.2f} m".format(alti))
    print("Sealevel Pressure = {0:0.2f} hPa".format(sea / 100))
    sleep(CYCLE)


