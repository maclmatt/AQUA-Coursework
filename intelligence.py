import numpy as np
from PIL import Image

def find_red_pixels(map_filename: str, upper_threshold=100, lower_threshold=50) -> list: #DONE 2 marks
    """Generates a binary image file, with the white pixels representing any red pixels in the original map

    Args:
        map_filename (str): filename of the map to find the red pixels in
        upper_threshold (int, optional): the minimum number the r value can be for the pixel to be considered red. Defaults to 100.
        lower_threshold (int, optional): the maximum number the g or b values can be for the pixel to be considered red. Defaults to 50.

    Returns:
        list: array of RGB values for new map representing the red pixels from the original map
    """
    
    im = Image.open("data/" + map_filename)
    pix = im.load()
    red_image_list = []

    for i in range(0, 1053):
        for j in range(0, 1140):
            pixel = pix[i, j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if (r > upper_threshold) and (g < lower_threshold) and (b < lower_threshold):
                red_image_list.append([255, 255, 255])
            else:
                red_image_list.append([3, 3, 3])

    red_image_np = np.array(red_image_list, dtype="uint8")
    red_image_np = np.reshape(red_image_np, (1053, 1140, 3))
    red_image = Image.fromarray(red_image_np)
    red_image = red_image.transpose(Image.Transpose.ROTATE_270)
    red_image = red_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if red_image.mode != 'RGB':
        red_image = red_image.convert('RGB')
    red_image.save("map-red-pixels.jpg")
    return red_image_np

def find_cyan_pixels(map_filename: str, upper_threshold=100, lower_threshold=50) -> list: #DONE 2 marks
    """Generates a binary image file, with the white pixels representing any cyan pixels in the original map

    Args:
        map_filename (str): filename of the map to find the cyan pixels in
        upper_threshold (int, optional): the minimum number the g and b values must be for the pixel to be considered cyan. Defaults to 100.
        lower_threshold (int, optional): the maximum number the r value can be for the pixel to be considered cyan. Defaults to 50.

    Returns:
        list: array of RGB values for new map representing the cyan pixels from the original map
    """
    
    im = Image.open("data/" + map_filename)
    pix = im.load()
    cyan_image_list = []

    for i in range(0, 1053):
        for j in range(0, 1140):
            pixel = pix[i, j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if (r < lower_threshold) and (g > upper_threshold) and (b > upper_threshold):
                cyan_image_list.append([255, 255, 255])
            else:
                cyan_image_list.append([3, 3, 3])

    cyan_image_np = np.array(cyan_image_list, dtype="uint8")
    cyan_image_np = np.reshape(cyan_image_np, (1053, 1140, 3))
    cyan_image = Image.fromarray(cyan_image_np)
    cyan_image = cyan_image.transpose(Image.Transpose.ROTATE_270)
    cyan_image = cyan_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if cyan_image.mode != 'RGB':
        cyan_image = cyan_image.convert('RGB')
    cyan_image.save("map-cyan-pixels.jpg")
    return cyan_image_np


find_cyan_pixels("map.png", 100, 50)


def detect_connected_components(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

