# Part Olly Programmed, implementing across devices and zoom

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ZoomScreen(Screen):
    def __init__(self, **kwargs):
        super(ZoomScreen, self).__init__(**kwargs)

        layout = Builder.load_file('zoom_screen.kv') # zoom_screen.kv created by Olly
        self.add_widget(layout)

    def loadImage(self):
        image_path = self.ids.imagePath.text
        self.ids.image.source = image_path
        self.ids.imagePath.text = ""