# Part Olly Programmed, implementing across devices and zoom
# worry about loading in later

# don't use kv file maybe

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from PIL import Image as PILImage 
from kivy.uix.label import Label
import cv2
import numpy as np
from load_image_zoom import create_image_buttons
from functools import partial

#Builder.load_file('zoom_screen.kv')

class ZoomScreen(Screen):
    #imagePath = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ZoomScreen, self).__init__(**kwargs)

        #layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        #layout = FloatLayout()
        # Wanna add image widget beside this as placeholder
        layout = GridLayout(cols=2, padding=20, spacing=3, cols_minimum={0: 100, 1: 100, 2:100, 3:100}, rows_minimum={0: 150, 1: 150, 3: 150})

        # add placeholder image widget that can then be replaced with loaded image
        # self.default_image = Image(source='elephant_balloon.jpg', size_hint=(None, None), height=400, width=700, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # layout.add_widget(self.default_image)

        # read in image as np array with cv2 library
        # use arrays then display them as images
        # manipulate first then convert

        # add to row then add row to layout
        # row = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint=(0.3,0.3), pos_hint={"x":1, "y":0})
        # layout.add_widget(row)
        # # #row2 = BoxLayout(orientation='horizontal', spacing=10, padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # row2 = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint=(0.3,0.3), pos_hint={"x":0.5, "y":0})
        # layout.add_widget(row2)
        self.default_image = 'elephant_balloon.jpg'
        self.get_image_buttons(layout)
        
        # color: color=(1,0,0,1) - this red
        load_label = Label(text='Enter an image path:')
        layout.add_widget(load_label)

        # should i be using self. ...
        self.load_textfield = TextInput(multiline=False)
        layout.add_widget(self.load_textfield)

        # # "Load Images" button
        load_button = Button(text='Load Images', on_press=partial(self.load_images, layout=layout))
        layout.add_widget(load_button)
        
        #"Back" button
        back_button = Button(text='Back to Main Page', on_press=self.go_back_to_main_page,)
        layout.add_widget(back_button)

        # #layout = Builder.load_file('zoom_screen.kv') # zoom_screen.kv created by Olly
        self.add_widget(layout)

    # Load image buttons with code from load_image_zoom.py
    def get_image_buttons(self, layout):
        create_image_buttons(self, layout)

    # def create_image_buttons(self, layout):
    #     # Read in default image as np array
    #     self.default = 'elephant_balloon.jpg'
    #     np_image = cv2.imread(self.default)
    #     np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
    #     h, w, c = np_image.shape
    #     # a quarter of the image will have half the rows and half the columns
    #     mid_height = h//2
    #     mid_width = w//2

    #     # Ones arrays for dividing up image into 4 quarters
    #     top_left = np.ones((mid_height,mid_width,c)).astype(np.uint8)
    #     top_right = np.ones((mid_height,mid_width,c)).astype(np.uint8)
    #     bottom_left = np.ones((mid_height,mid_width,c)).astype(np.uint8)
    #     bottom_right = np.ones((mid_height,mid_width,c)).astype(np.uint8)

    #     # taking all rows and all columns in correct range
    #     # top left quadrant of image is from start at 0 to middle of image regarding height
    #     # from 0 to middle of image regarding width
    #     top_left[:,:,:] = np_image[0:mid_height, 0:mid_width, :].astype(np.uint8)
    #     top_right[:,:,:] = np_image[0:mid_height, mid_width:w, :].astype(np.uint8)
    #     bottom_left[:,:,:] = np_image[mid_height:h, 0:mid_width, :].astype(np.uint8)
    #     # bottom right is from pixel after mid point regarding height till the end of the image
    #     # from pixel after midpoint regarding width till end of image
    #     bottom_right[:,:,:] = np_image[mid_height:h, mid_width:w, :].astype(np.uint8)
    #     #top_left = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)

    #     top_left = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)
    #     top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)
    #     bottom_left = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB)
    #     bottom_right = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB)
    #     cv2.imwrite('top_left.png', top_left)
    #     cv2.imwrite('top_right.png', top_right)
    #     cv2.imwrite('bottom_left.png', bottom_left)
    #     cv2.imwrite('bottom_right.png', bottom_right)
    #     image_button_top_left = Button(background_normal='top_left.png')
    #     layout.add_widget(image_button_top_left)
    #     image_button_top_right = Button(background_normal='top_right.png')
    #     layout.add_widget(image_button_top_right)
    #     image_button_bottom_left = Button(background_normal='bottom_left.png')
    #     layout.add_widget(image_button_bottom_left)
    #     image_button_bottom_right = Button(background_normal='bottom_right.png')
    #     layout.add_widget(image_button_bottom_right)

    # have image loaded in, need to place click areas over image based on array of pixels?
    def load_images(self, instance, layout):
        image_path = self.load_textfield.text
        # works right but arrays made and buttons filled once and not again
        # need those to happen here?
        self.default_image = image_path
        print(image_path)
        # change this so not using kv file

        # when press load want to read inputted path and load that path
        # image = Image(source='elephant_balloon.jpg')
        # image_layout.add_widget(image)
        print("loaded")
        self.get_image_buttons(layout)

        # imagePath = self.ids.imagePath.text
        # #imagePath = self.imagePath.text
        # self.ids.image.source = imagePath
        # #self.ids.imagePath.text = ""
        # self.imagePath.text = ""

    def go_back_to_main_page(self, instance):
        self.manager.current = 'home'
