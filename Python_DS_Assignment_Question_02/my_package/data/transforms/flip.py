#Imports
import PIL
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if self.flip_type=="vertical":
            image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        else:
            image= image.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        return image 
