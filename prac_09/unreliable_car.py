from prac_09.car import Car
from random import randint


class Unreliable_Car(Car):
    """Specialised version of Car that may randomly not drive"""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance based on the Car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent car but only if a random integer is less than the reliability."""
        distance_driven = 0
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
