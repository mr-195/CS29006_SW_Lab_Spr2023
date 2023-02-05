# Imports
from random import randrange
from PIL import Image

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if self.crop_type == "center":
            width,height = image.size()
            left = (width -self.shape.w)/2
            top = (height - self.shape.h)/2
            right = (width + self.shape.w)/2
            bottom = (height + self.shape.h)/2
            # Crop the center of the image
            image = image.crop((left, top, right, bottom))

        else:
            print("You've chosen to do random cropping: Please enter the matrix size for your final image (x and y separately)")
            matrix1 = int(input())
            matrix2 = int(input())
            x, y = image.size
            x1 = randrange(0, x - matrix1)
            y1 = randrange(0, y - matrix2)
            image = image.crop(x1, y1, x1 + matrix1, y1 + matrix2)
        return image