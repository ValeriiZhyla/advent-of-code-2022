from .point import Point
from .sensor import Sensor
import re


class SensorReportParser:
    def parse(self, input: list[str]) -> list[Sensor]:
        sensors: list[Sensor] = []
        for line in input:
            numbers = [int(d) for d in re.findall(r'-?\d+', line)]
            assert len(numbers) == 4
            sensors.append(Sensor(Point(numbers[0], numbers[1]), Point(numbers[2], numbers[3])))
        return sensors
