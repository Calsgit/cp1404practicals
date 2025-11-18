from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of taxi with extra fanciness and fares."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise the silverservicetaxi based on Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like taxi with added flagfall."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2}"
