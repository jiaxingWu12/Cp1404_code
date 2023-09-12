from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        self.root.ids.entries_box.clear_widgets()  # Clear existing labels
        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()

DynamicLabelsApp().run()
