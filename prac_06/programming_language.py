class ProgrammingLanguage:
    """Represent a programming language and some basic information of it."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance.
        name: string, name of language
        typing: string, 'Static' or 'Dynamic'
        reflection: boolean
        year: string, year the language was released
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine whether the programming language has dynamic typing"""
        return 'dynamic' in self.typing.lower()

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
