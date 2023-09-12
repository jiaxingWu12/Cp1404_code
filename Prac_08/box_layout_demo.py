from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("Greet")
        output_label = self.root.ides.putput_label
        input_name = self.root.ids.input_name
        output_label.txt = f"Hello{input_name.text}"

    def handle_clear(self):
        print("Clear")
        output_label = self.root.ids.output_label
        input_name = self.root.ids.input_name
        output_label.text = ""
        input_name.text = ""


BoxLayoutDemo().run()