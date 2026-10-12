from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class TombolAngka(Label):
    def __init__(self, kalkulator, **kwargs):
        super().__init__(**kwargs)
        self.kalkulator = kalkulator
        self.font_size = 28

    def on_press(self):
        self.kalkulator.input_text += self.text
        self.kalkulator.update_display()



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))

        return sm













app = MyApp()
app.run()