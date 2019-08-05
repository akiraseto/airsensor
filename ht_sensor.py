import Adafruit_DHT as DHT
import sys

PIN = 4
humi, temp = DHT.read_retry(DHT.DHT11, PIN)

if humi == None or temp == None:
    print("DHT11 Connection is Broken..")
    sys.exit(0)
else:
    print("DHT11 Sensor start ")

def run():
    if (humi > 90) or (temp > 50):
        print("error value:", humi, temp)

    return temp, humi
