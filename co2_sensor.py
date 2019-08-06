import qwiic_ccs811
import sys

class Co2Sensor:

    def __init__(self):
        self.sensor = qwiic_ccs811.QwiicCcs811()
        if self.sensor.is_connected() == False:
            print("CCS811 Sensor isn't connected to the system. Please check your connection", file=sys.stderr)
            sys.exit(0)
        else:
            print("CCS811 Sensor start")
            self.sensor.begin()

    def run(self):
        self.sensor.read_algorithm_results()
        co2 = self.sensor.get_co2()
        tvoc = self.sensor.get_tvoc()

        return co2, tvoc

