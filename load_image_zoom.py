import numpy as np
import cv2
from kivy.uix.button import Button

# Takes self of zoom screen class and a layout, generating image buttons
# for that layout

# shape mismatch error when loading in tiger
def create_image_buttons(self, layout):
    # Read in default image as np array
    np_image = cv2.imread(self.default_image)
    print(self.default_image)
    np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
    h, w, c = np_image.shape
    # a quarter of the image will have half the rows and half the columns
    mid_height = h//2
    mid_width = w//2

    # taking all rows and all columns in correct range
    # top left quadrant of image is from start at 0 to middle of image regarding height
    # from 0 to middle of image regarding width
    top_left = np_image[0:mid_height, 0:mid_width, :].astype(np.uint8)
    top_right = np_image[0:mid_height, mid_width:w, :].astype(np.uint8)
    bottom_left = np_image[mid_height:h, 0:mid_width, :].astype(np.uint8)
    # bottom right is from pixel after mid point regarding height till the end of the image
    # from pixel after midpoint regarding width till end of image
    bottom_right = np_image[mid_height:h, mid_width:w, :].astype(np.uint8)

    top_left = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)
    top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)
    bottom_left = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB)
    bottom_right = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB)

    cv2.imwrite('top_left.png', top_left)
    cv2.imwrite('top_right.png', top_right)
    cv2.imwrite('bottom_left.png', bottom_left)
    cv2.imwrite('bottom_right.png', bottom_right)
