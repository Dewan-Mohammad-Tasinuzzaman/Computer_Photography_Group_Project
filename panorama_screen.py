# Part programmed by Dewan. Panorama creation.

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from PIL import Image as PILImage  # Importing Image module from PIL

class PanoramaScreen(Screen):
    def __init__(self, **kwargs):
        super(PanoramaScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Creating TextInput widgets for user to input image names
        self.image_inputs = []
        for i in range(3):
            image_input = TextInput(
                multiline=False, 
                hint_text=f"Enter Image {i + 1} File Name (e.g., image{i + 1}.jpg)",
                size_hint=(1, None),
                height=30
            )
            self.image_inputs.append(image_input)
            layout.add_widget(image_input)

        # Creating Image widgets for displaying loaded images
        self.image_widgets = []

        # Image widgets (side by side)
        image_layout = BoxLayout(orientation='horizontal', spacing=10)
        for i in range(3):
            img_widget = Image(source="", size=(300, 200), allow_stretch=True)
            self.image_widgets.append(img_widget)
            image_layout.add_widget(img_widget)
        layout.add_widget(image_layout)

        # "Load Images" button
        load_button = Button(text='Load Images', on_press=self.load_images)
        layout.add_widget(load_button)

        # "Generate Panorama" button
        generate_button = Button(text='Generate Panorama', on_press=self.generate_panorama)
        layout.add_widget(generate_button)

        # "Back" button
        back_button = Button(text='Back to Main Page', on_press=self.go_back_to_main_page)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def load_images(self, instance):
        # Iterate through TextInput widgets and corresponding Image widgets
        for i, (img_widget, input_widget) in enumerate(zip(self.image_widgets, self.image_inputs)):
            # Get input text from the TextInput widget
            image_name = input_widget.text.strip()

            # Check that image_name is not empty
            if image_name:
                # Loading image and updating the Image widget
                img_widget.source = image_name

    def generate_panorama(self, instance):
        # the paths of the three input images
        image_paths = [input_widget.text.strip() for input_widget in self.image_inputs]

        if all(image_paths):
            # Open the images using PIL
            images = [PILImage.open(image_path) for image_path in image_paths]

            # Getting size of the first image
            width, height = images[0].size

            # Creating a new image with triple width (3 * Width of Each Image)
            panorama = PILImage.new('RGB', (width * 3, height))

            # Pasting the images side by side to create the panorama
            panorama.paste(images[0], (0, 0))
            panorama.paste(images[1], (width, 0))
            panorama.paste(images[2], (width * 2, 0))

            # Display panorama image
            panorama.show()
            # Save the panorama image
            panorama.save("panorama_result.jpg")

    def go_back_to_main_page(self, instance):
        self.manager.current = 'home'
