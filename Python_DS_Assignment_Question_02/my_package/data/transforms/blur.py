# Imports
from PIL import Image, ImageFilter


class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Opens a image in RGB mode

        im = Image.open("geek.jpg")

        # Blurring the image
        im1 = im.filter(ImageFilter.GaussianBlur(4))

        # Shows the image in image viewer
        im1.show()
