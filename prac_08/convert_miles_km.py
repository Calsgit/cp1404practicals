"""Convert miles to Km
Time estimate: 20 min
Time elapsed:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATIO = 1.60934


class Convert_Miles_Km(App):
    """Convert_Miles_Km is an app for converting a value in miles to kilometres."""
    output = StringProperty()  # I don't understand this

    def build(self):
        """Build the kivy app from the corresponding kv file."""
        self.title = "Convert miles to kilometres"
        self.output = '0'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_up(self):
        try:
            self.root.ids.input_text.text = str(float(self.root.ids.input_text.text) + 1)
        except ValueError:
            self.root.ids.input_text.text = '0'

    def handle_down(self):
        try:
            self.root.ids.input_text.text = str(float(self.root.ids.input_text.text) - 1)
        except ValueError:
            self.root.ids.input_text.text = '0'

    def handle_convert(self):
        self.output = str(float(self.root.ids.input_text.text) * MILES_TO_KM_RATIO)


Convert_Miles_Km().run()
