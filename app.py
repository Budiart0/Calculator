from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        return sm













app = MyApp()
app.run()