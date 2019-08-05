import qwiic_ccs811
import sys

mySensor = qwiic_ccs811.QwiicCcs811()

if mySensor.is_connected() == False:
    print("CCS811 Sensor isn't connected to the system. Please check your connection", file=sys.stderr)
    sys.exit(0)
else:
    print("CCS811 Sensor start")
    mySensor.begin()

def run():

    mySensor.read_algorithm_results()
    co2 = mySensor.get_co2()
    tvoc = mySensor.get_tvoc()

    return co2, tvoc

