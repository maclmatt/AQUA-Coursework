import numpy as np
from PIL import Image
from utils import countvalue, maxvalue

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
    width, height = im.size
    red_image_list = np.empty((width, height, 3), dtype="uint8")

    for i in range(0, width):
        for j in range(0, height):
            pixel = pix[i, j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if (r > upper_threshold) and (g < lower_threshold) and (b < lower_threshold):
                red_image_list[i][j] = [255, 255, 255]
            else:
                red_image_list[i][j] = [0, 0, 0]

    #red_image_list = np.array(red_image_list, dtype="uint8")
    #red_image_np = np.reshape(red_image_np, (width, height, 3))
    red_image = Image.fromarray(red_image_list)
    red_image = red_image.transpose(Image.Transpose.ROTATE_270)
    red_image = red_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if red_image.mode != 'RGB':
        red_image = red_image.convert('RGB')
    red_image.save("map-red-pixels.jpg")
    return red_image_list

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
                cyan_image_list.append([0, 0, 0])

    cyan_image_np = np.array(cyan_image_list, dtype="uint8")
    cyan_image_np = np.reshape(cyan_image_np, (1053, 1140, 3))
    cyan_image = Image.fromarray(cyan_image_np)
    cyan_image = cyan_image.transpose(Image.Transpose.ROTATE_270)
    cyan_image = cyan_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if cyan_image.mode != 'RGB':
        cyan_image = cyan_image.convert('RGB')
    cyan_image.save("map-cyan-pixels.jpg")
    return cyan_image_np

def detect_connected_components(image: list):
    """Your documentation goes here"""

    width = len(image)
    height = len(image[0])

    MARK = np.full((width, height), 0)

    Q = []
    WHITE = np.array([255, 255, 255])
    conncomponentscount = 1
    conncomponents = []

    for j in range(0, height):
        for i in range(0, width):
            if np.array_equal(image[i][j], WHITE) and (MARK[i][j] == 0):
                MARK[i][j] = conncomponentscount
                connected = False
                Q.append((i, j))
                while Q != []:
                    q = Q.pop(0)
                    x = q[0]
                    y = q[1]
                    n = []
                    for m in range(-1, 2):
                        for k in range(-1, 2):
                            nx = x + m
                            ny = y + k
                            if ((nx > -1) and (nx < width)) and ((ny > -1) and (ny < height)):
                                n.append((nx, ny))
                    for each in n:
                        if np.array_equal(image[each[0]][each[1]], WHITE) and (MARK[each[0]][each[1]] == 0):
                            MARK[each[0]][each[1]] = conncomponentscount
                            connected = True
                            Q.append((each[0], each[1]))

                if not connected:
                    MARK[i][j] = -1
                else:
                    conncomponentscount += 1

    for i in range(1, conncomponentscount):
        regionsize = 0
        for every in MARK:
            for each in every:
                if each == i:
                    regionsize += 1
        if regionsize > 0:
            conncomponents.append((i, regionsize))

    f = open("cc-output-2a.txt", "a")
    for each in conncomponents:
        f.write("Connected Component " + str(each[0]) + ", number of pixels = " + str(each[1]) + "\n")
    f.write("Total number of connected components = " + str(conncomponentscount - 1))
    f.close()
            
    return MARK

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

red_pixels = find_red_pixels("map.png")
MARK = detect_connected_components(red_pixels)