import datetime


class Guitar:
    """Represent a guitar and its characteristics."""

    def __init__(self, name="", year=0, cost=0):
        """
        name: string, name of guitar
        year: int, year guitar was made
        cost: float, price of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar based on the year it was made."""
        return datetime.date.today().year - self.year

    def is_vintage(self):
        """Determine whether the guitar is 50+ years old"""
        return self.get_age() >= 50
