class Project:
    """Defines a project."""

    def __init__(self, name, start_date, priority=1, cost_estimate=0.0, completion_percentage=0):
        """Set definitions for the class."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
