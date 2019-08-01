from __future__ import print_function
import qwiic_ccs811
import time
import sys
from datetime import datetime

def runExample():
    print("\nCCS811 Sensor start \n")
    mySensor = qwiic_ccs811.QwiicCcs811()

    if mySensor.is_connected() == False:
        print("CCS811 Sensor isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    mySensor.begin()

    while True:
        mySensor.read_algorithm_results()
        print("+", datetime.now().strftime('%H:%M:%S'), "----")
        print("CO2 = {0:0.2f} ppm".format(mySensor.get_co2()))
        print("TVOC = {0:0.2f} ppb".format(mySensor.get_tvoc()))
        time.sleep(5)


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Basic Example")
        sys.exit(0)
