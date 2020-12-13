from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print(f"Mouse down at {touch}")
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print(f"Mouse move at {touch}")

    def on_touch_up(self, touch):
        print(f"Mouse up at {touch}")
        self.btn.opacity = 1


class MyApp2(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyApp2().run()
