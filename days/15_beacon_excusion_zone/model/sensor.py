from .point import Point


class Sensor:
    sensor_coordinate: Point = None
    closest_beacon_coordinate: Point = None
    manhattan_distance: int = 0

    def __init__(self, sensor_coordinate: Point, closest_beacon_coordinate: Point):
        self.sensor_coordinate = sensor_coordinate
        self.closest_beacon_coordinate = closest_beacon_coordinate
        self.manhattan_distance = sensor_coordinate.calculate_manhattan_distance_to(closest_beacon_coordinate)


