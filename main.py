# Part Dewan Programmed. Overall setup for the application's UI.

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home_screen import HomeScreen
from zoom_screen import ZoomScreen
from panorama_screen import PanoramaScreen  # Add this line

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ZoomScreen(name='zoom'))
        sm.add_widget(PanoramaScreen(name='panorama'))  # Add this line
        return sm

if __name__ == '__main__':
    MyApp().run()
