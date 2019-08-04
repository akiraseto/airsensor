import Adafruit_BMP.BMP085 as BMP085
import sys

try:
    sensor = BMP085.BMP085()
except:
    print("\nBMP180 Connection is Broken..\n")
    sys.exit(0)
else:
    print("\nBMP180 Sensor start \n")

def run():
    temp = sensor.read_temperature()
    press = sensor.read_pressure()
    alti = sensor.read_altitude()
    sea = sensor.read_sealevel_pressure()

    if (temp > 55) or (press > 110000) or (press < 90000) or (alti > 3776):
        print("error value:", temp, press, alti, sea)

    return temp, press, alti, sea
