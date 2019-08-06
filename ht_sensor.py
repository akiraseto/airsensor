import Adafruit_DHT as DHT
import sys

class DhtSensor:

    def __init__(self):
        PIN = 4
        self.humi, self.temp = DHT.read_retry(DHT.DHT11, PIN)

        if self.humi == None or self.temp == None:
            print("DHT11 Connection is Broken..")
            sys.exit(0)
        else:
            print("DHT11 Sensor start ")

    def run(self):
        if (self.humi > 90) or (self.temp > 50):
            print("error value:", self.humi, self.temp)

        return self.temp, self.humi
