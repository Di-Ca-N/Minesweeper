import os
import wx

IMAGES_DIR = os.path.dirname(__file__)
BOMB_IMAGE_PATH = os.path.join(IMAGES_DIR, 'bomb.png')
FLAG_IMAGE_PATH = os.path.join(IMAGES_DIR, 'flag.png')
CLOSED_IMAGE_PATH = os.path.join(IMAGES_DIR, 'closed.png')


def get_images(size):
    return {
        'BOMB': scale(BOMB_IMAGE_PATH, size),
        'FLAG': scale(FLAG_IMAGE_PATH, size),
        'CLOSED': scale(CLOSED_IMAGE_PATH, size),
    }


def scale(image_path, size):
    image = wx.Image(image_path)
    image.Rescale(*size)
    return wx.Bitmap(image)
