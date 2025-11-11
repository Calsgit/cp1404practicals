"""Convert miles to Km
Time estimate: 20 min
Time elapsed:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class Convert_Miles_Km(App):
    """Convert_Miles_Km is an app for converting a value in miles to kilometres."""
    def build(self):
        """Build the kivy app from the corresponding kv file."""
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root