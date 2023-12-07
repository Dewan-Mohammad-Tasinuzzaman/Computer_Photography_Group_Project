from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home_screen import HomeScreen
from zoom_screen import ZoomScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ZoomScreen(name='zoom'))
        return sm

if __name__ == '__main__':
    MyApp().run()
