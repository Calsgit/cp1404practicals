class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a band with name and empty member list."""
        self.name = name
        self.members = []

    def add(self, member):
        """Add a member to the band's member list."""
        self.members.append(member)
