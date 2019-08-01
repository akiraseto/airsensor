import Adafruit_BMP.BMP085 as BMP085
import time
from datetime import datetime

print("\nBMP180 Sensor start \n")
sensor = BMP085.BMP085()

while True:
    print("+", datetime.now().strftime('%H:%M:%S'), "----")
    print("Temp = {0:0.2f} *C".format(sensor.read_temperature()))
    print("Pressure = {0:0.2f} hPa".format(sensor.read_pressure() / 100))
    print("Altitude = {0:0.2f} m".format(sensor.read_altitude()))
    print("Sealevel Pressure = {0:0.2f} hPa".format(sensor.read_sealevel_pressure() / 100))
    time.sleep(5)


