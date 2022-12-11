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
    WIDTH, HEIGHT = im.size
    red_image_list = np.empty((WIDTH, HEIGHT, 3), dtype="uint8")

    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            pixel = pix[i, j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if (r > upper_threshold) and (g < lower_threshold) and (b < lower_threshold):
                red_image_list[i][j] = [255, 255, 255]
            else:
                red_image_list[i][j] = [0, 0, 0]

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
    WIDTH, HEIGHT = im.size
    cyan_image_list = np.empty((WIDTH, HEIGHT, 3), dtype="uint8")

    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            pixel = pix[i, j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if (r < lower_threshold) and (g > upper_threshold) and (b > upper_threshold):
                cyan_image_list[i][j] = [255, 255, 255]
            else:
                cyan_image_list[i][j] = [0, 0, 0]

    cyan_image = Image.fromarray(cyan_image_list)
    cyan_image = cyan_image.transpose(Image.Transpose.ROTATE_270)
    cyan_image = cyan_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if cyan_image.mode != 'RGB':
        cyan_image = cyan_image.convert('RGB')
    cyan_image.save("map-cyan-pixels.jpg")
    return cyan_image_list

def detect_connected_components(image: list) -> list: #DONE 12 marks
    """Finds all 8-connected components, where there are adjacent white pixels

    Args:
        image (list): 3D array of all pixels from black and white image 

    Returns:
        list: 3D array of all pixels, with each value representing whether they are connected to a 
        connected component region or not. 
            Value 0 means the pixel is black, 
            -1 means the pixel is white but not connected to any other white pixels and 
            a positive number means the pixel is white and connected to other white pixel, 
                with the number relating to the number of connnected regions in the image
    """

    #All modifications to ALgorithm 1 marked 'MOD'

    WIDTH = len(image)
    HEIGHT = len(image[0])
    WHITE = np.array([255, 255, 255])
    MARK = np.full((WIDTH, HEIGHT), 0)
    Q = []
    global conncomponentscount
    conncomponentscount = 1
    conncomponents = []

    for j in range(0, HEIGHT):
        for i in range(0, WIDTH):
            if np.array_equal(image[i][j], WHITE) and (MARK[i][j] == 0):
                MARK[i][j] = conncomponentscount    #MOD: pixel now assigned the Connected Copmonent number
                #MOD: boolean variable added, shows whether a 2nd white pixel has been found that connects to image[i][j]
                connected = False
                Q.append([i, j])
                while Q != []:
                    q = Q.pop(0)
                    x = q[0]
                    y = q[1]
                    n = []
                    #MOD: double for loop added, to find all 8 neighbours of image[i][j]
                    for m in range(-1, 2):
                        for k in range(-1, 2):
                            nx = x + m
                            ny = y + k
                            if ((nx > -1) and (nx < WIDTH)) and ((ny > -1) and (ny < HEIGHT)):
                                n.append([nx, ny])
                    for each in n:
                        if np.array_equal(image[each[0]][each[1]], WHITE) and (MARK[each[0]][each[1]] == 0):
                            MARK[each[0]][each[1]] = conncomponentscount #MOD: pixel now assigned the Connected Copmonent number
                            connected = True
                            Q.append([each[0], each[1]])

                if not connected:
                    #MOD: changes MARK[i][j] to -1 if there were no other white pixels connected to it
                    MARK[i][j] = -1
                else:
                    conncomponentscount += 1

    #MOD: runs through all elements in MARK to find all connected components and their size.
    for i in range(1, conncomponentscount):
        regionsize = 0
        for every in MARK:
            for each in every:
                if each == i:
                    regionsize += 1
        if regionsize > 0:
            conncomponents.append([i, regionsize])

    #MOD: writes all connected components to file
    f = open("cc-output-2a.txt", "w")
    f.close()
    f = open("cc-output-2a.txt", "a")
    for each in conncomponents:
        f.write("Connected Component " + str(each[0]) + ", number of pixels = " + str(each[1]) + "\n")
    f.write("Total number of connected components = " + str(conncomponentscount - 1))
    f.close()
            
    return MARK

def detect_connected_components_sorted(MARK: list): #DONE 4 marks
    """Sorts all connected components into descending order, and generates image of the two largest connected components

    Args:
        MARK (list): 3D array of all pixels, with each value representing whether they are connected to a 
        connected component region or not. 
            Value 0 means the pixel is black, 
            -1 means the pixel is white but not connected to any other white pixels and 
            a positive number means the pixel is white and connected to other white pixel, 
                with the number relating to the number of connnected regions in the image
    """
    
    conncomponents = []
    for i in range(1, 224):
        regionsize = 0
        for every in MARK:
            for each in every:
                if each == i:
                    regionsize += 1
        if regionsize > 0:
            conncomponents.append([i, regionsize])

    L = conncomponents
    Lsorted = False
    while not Lsorted:
        swapped = False
        for i in range (len(L) -1):
            if L[i][1] < L[i + 1][1]:
                L[i + 1] , L[i] = L[i] , L[i + 1]
                swapped = True
        if not swapped:
            Lsorted = True

    f = open("cc-output-2b.txt", "w")
    f.close()
    f = open("cc-output-2b.txt", "a")
    for each in L:
        f.write("Connected Component " + str(each[0]) + ", number of pixels = " + str(each[1]) + "\n")
    f.write("Total number of connected components = " + str(223))
    f.close()

    a = L[0][0]
    b = L[1][0]
    WIDTH = 1053
    HEIGHT = 1140

    largest_comps_list = np.empty((WIDTH, HEIGHT, 3), dtype="uint8")

    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            if (MARK[i][j] == a) or (MARK[i][j] == b):
                largest_comps_list[i][j] = [255, 255, 255]
            else:
                largest_comps_list[i][j] = [0, 0, 0]

    largest_comps = Image.fromarray(largest_comps_list)
    largest_comps = largest_comps.transpose(Image.Transpose.ROTATE_270)
    largest_comps = largest_comps.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if largest_comps.mode != 'RGB':
        largest_comps = largest_comps.convert('RGB')
    largest_comps.save("cc-top-2.jpg")
    

red_pixels = find_red_pixels("map.png")
MARK = detect_connected_components(red_pixels)

detect_connected_components_sorted(MARK)