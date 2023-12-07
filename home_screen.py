from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        heading = Label(text="Computer Photography - Group Project - Fall 2023", font_size=24)
        zoom_button = Button(text="Image Zooming", on_press=self.go_to_zoom_screen)

        layout.add_widget(heading)
        layout.add_widget(zoom_button)

        self.add_widget(layout)

    def go_to_zoom_screen(self, instance):
        self.manager.current = 'zoom'
