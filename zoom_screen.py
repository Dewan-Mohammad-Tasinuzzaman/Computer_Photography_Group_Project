# Part Olly Programmed, implementing across devices and zoom
# worry about loading in later

# don't use kv file maybe

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from PIL import Image as PILImage 
from kivy.uix.label import Label
import cv2
import numpy as np

#Builder.load_file('zoom_screen.kv')

class ZoomScreen(Screen):
    #imagePath = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ZoomScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # add placeholder image widget that can then be replaced with loaded image
        self.default_image = Image(source='elephant_balloon.jpg', size_hint=(None, None), height=400, width=700, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.default_image)

        # Will this work when image path gets updated?

        # read in image as np array with cv2 library
        # use arrays then display them as images
        # manipulate first then convert
        default = 'elephant_balloon.jpg'
        np_image = cv2.imread(default)
        np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
        h, w, c = np_image.shape
        print(c)
        mid_height = h//2
        mid_width = w//2

        # a quarter of the image will have half the rows and half the columns
        top_left = np.ones((mid_height,mid_width,c))
        top_right = np.ones((mid_height,mid_width,c))
        bottom_left = np.ones((mid_height,mid_width,c))
        bottom_right = np.ones((mid_height,mid_width,c))
        print(top_left)

        # taking all rows and all columns in correct range
        # top left quadrant of image is from start at 0 to middle of image regarding height
        # from 0 to middle of image regarding width
        
        
        # top_left[:,:,:] = np_image[0:mid_height, 0:mid_width, c]
        # top_right[:,:,:] = np_image[0:mid_height, (mid_height+1):w, c]
        # bottom_left[:,:,:] = np_image[((mid_height)+1):h, 0:mid_width, c]
        # # bottom right is from pixel after mid point regarding height till the end of the image
        # # from pixel after midpoint regarding width till end of image
        # bottom_right[:,:,:] = np_image[((mid_height)+1):h, mid_width:w, c]
        # print(top_left)
        # print(top_right)
        # print(bottom_left)
        # print(bottom_right)

        # divide image up into 4 quarters, then fill up arrays with those 4 quarters

        # wanna divide image up into 4 seperate ones attached together, and turn those each into buttons
        
        # color: color=(1,0,0,1) - this red
        load_label = Label(text='Enter an image path:')
        layout.add_widget(load_label)

        # should i be using self. ...
        self.load_textfield = TextInput(multiline=False, size_hint=(None, None), height=30, width = 200)
        layout.add_widget(self.load_textfield)

        # # "Load Images" button
        load_button = Button(text='Load Images', on_press=self.load_images)
        layout.add_widget(load_button)
        
        # # "Back" button
        back_button = Button(text='Back to Main Page', on_press=self.go_back_to_main_page)
        layout.add_widget(back_button)

        # #layout = Builder.load_file('zoom_screen.kv') # zoom_screen.kv created by Olly
        self.add_widget(layout)

    # have image loaded in, need to place click areas over image based on array of pixels?
    def load_images(self, instance):
        image_path = self.load_textfield.text
        self.default_image.source = image_path
        print(image_path)
        # change this so not using kv file

        # when press load want to read inputted path and load that path
        # image = Image(source='elephant_balloon.jpg')
        # image_layout.add_widget(image)
        print("loaded")

        # imagePath = self.ids.imagePath.text
        # #imagePath = self.imagePath.text
        # self.ids.image.source = imagePath
        # #self.ids.imagePath.text = ""
        # self.imagePath.text = ""

    def go_back_to_main_page(self, instance):
        self.manager.current = 'home'
