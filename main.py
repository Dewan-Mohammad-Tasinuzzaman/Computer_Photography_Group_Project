# Part Dewan Programmed. For overall setup for the application's UI.

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home_screen import HomeScreen
from zoom_screen import ZoomScreen
from panorama_screen import PanoramaScreen
from depth_estimation_screen import DepthEstimationScreen
from object_removal_screen import ObjectRemovalScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ZoomScreen(name='zoom'))
        sm.add_widget(PanoramaScreen(name='panorama'))
        sm.add_widget(DepthEstimationScreen(name='depth_estimation'))
        sm.add_widget(ObjectRemovalScreen(name='object_removal'))
        return sm

if __name__ == '__main__':
    MyApp().run()
