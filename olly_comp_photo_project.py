# Part Olly Programmed, implementing across devices and zoom
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup

Builder.load_file('olly_photo_project.kv')

class LoadLayout(Popup):
    imagePath = ObjectProperty(None)

    def stuff(self):
        print("stuff")

    def submit(self):
        imagePath = self.imagePath.text
        print(imagePath)
        self.imagePath.text = ""
        self.dismiss()
        
class MyLayout(Widget):
    imagePath = ObjectProperty(None)
    #image = ObjectProperty(None)

    def loadImage(self):
        imagePath = self.imagePath.text
        self.ids.image.source = imagePath
        #print(imagePath)
        self.imagePath.text = ""

    # Exit
    def exitPress(self):
        App.get_running_app().stop()

class MyApp(App):
    def build(self):
        # Set background of window to white and give title
        Window.clearcolor = (1,1,1,1)
        self.title = "Olly's Zooming"
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()