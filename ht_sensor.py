import Adafruit_DHT as DHT
import sys

PIN = 4
humi, temp = DHT.read_retry(DHT.DHT11, PIN)

if humi == None or temp == None:
    print("\nDHT11 Connection is Broken..\n")
    sys.exit(0)
else:
    print("\nDHT11 Sensor start \n")

def run():
    if (humi > 90) or (temp > 50):
        print("error value:", humi, temp)

    return temp, humi
