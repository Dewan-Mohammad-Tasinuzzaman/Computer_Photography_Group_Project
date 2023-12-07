# Programmed by "Huzefa Ali Asgar"

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ObjectRemovalScreen(Screen):
    def __init__(self, **kwargs):
        super(ObjectRemovalScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        heading = Label(text="Object Removal Page", font_size=24)
        back_button = Button(text="Back to Home", on_press=self.go_back_to_home)

        layout.add_widget(heading)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back_to_home(self, instance):
        self.manager.current = 'home'
