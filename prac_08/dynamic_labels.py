"""Dynamic labels
Time estimate: 20 min
Time elapsed: 30 min
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ("me", "you", "them", "him", "her", "the guy on the side of the road")

class dynamic_labels(App):
    """Dynamic labels is a simple kivy app used for testing adding dynamic labels to the UI."""

    def build(self):
        """Build the kivy app from the corresponding kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in NAMES:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)



dynamic_labels().run()
