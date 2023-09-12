from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class SquareNumberApp(App):
    def build(self):
        Window.size = (400, 200)  # Increased window size to accommodate the changes
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

if __name__ == "__main__":
    SquareNumberApp().run()
