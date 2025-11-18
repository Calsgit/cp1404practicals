from prac_09.car import Car


class Unreliable_Car(Car):
    """Specialised version of Car that may randomly not drive"""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance based on the Car class."""
        super().__init__(name, fuel)
        self.reliability = reliability
