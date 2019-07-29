from __future__ import print_function
import qwiic_ccs811
import time
import sys


def runExample():
    print("\nSparkFun CCS811 Sensor Basic Example \n")
    mySensor = qwiic_ccs811.QwiicCcs811()

    if mySensor.is_connected() == False:
        print("The Qwiic CCS811 device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    mySensor.begin()

    while True:
        mySensor.read_algorithm_results()
        print("CO2:\t%.3f" % mySensor.get_co2())
        print("TVOC:\t%.3f\n" % mySensor.get_tvoc())
        time.sleep(1)


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Basic Example")
        sys.exit(0)
