##comes from reporting.py marker 1
#datestring = "2021-01-01"
#date = datetime.datetime(2021, 1, 1)

##comes from reporting.py marker 2
        #nextdate = date + datetime.timedelta(days=1)




        #line_count = 1
        #daily_averages = []
        #sumofpollutant = 0
        #for row in csv_reader:
            #if line_count < 24:
                #sumofpollutant += row[pollutantindex]
                #line_count += 1
            #elif line_count == 24:
                #daily_averages.append(sumofpollutant/24)
                #line_count = 1
                #sumofpollutant = 0

##median and mean testing
#list1 = [22.453, 19.099, 20.925, 19.974, 17.363, 12.434, 13.316,13.335,16.811,19.01,21.757,22.738,24.545,27.694,25.764,22.068,22.229,20.708,19.385,16.995,14.024,11.314,7.723,6.831]
#list1.sort()
#print(list1)

##learning numpy
#import numpy as np

#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#newarr = arr.reshape(2, 3, 2)

#print(newarr)


#arr = np.array([1, 2, 3, 4, 5, 4, 4])

#x = np.where(arr == 4)

#print(x[0][0])

#arr = np.array([6, 7, 8, 9])

#x = np.searchsorted(arr, 7, side='right')

#print(x)

#arr = np.array([1, 3, 5, 7])

#x = np.searchsorted(arr, [2, 4, 6])
#arr[arr == 1] = 3
#print(arr)

#for i in range(1, 3):
    #print(i)

import matplotlib.pyplot as plt
import numpy as np
from intelligence import find_red_pixels

#image = plt.imread("data/map.png", format=None)
#print(image[555][500])
#plt.imshow(image)
#plt.show()

find_red_pixels("map.png", 100, 50)

##from intelligence.py line 8, before image processing changes made
image = plt.imread("data/" + map_filename, format=None)

red_image = np.empty((1140, 1053))

    
row_count = 0
for row in image:
    for pixel in row:
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        if (r > upper_threshold) and (g < lower_threshold) and (b < lower_threshold):
        print("hi")
            np.append(red_image[row_count], [255, 255, 255, 1])
        else:
            np.append(red_image[row_count], [0, 0, 0, 1])
    row_count += 1
plt.imshow(red_image)
plt.show()

#line29
im1 = Image.fromarray(red_image1)
    if im1.mode != 'RGB':
        im1 = im1.convert('RGB')
    im1.save("map-red-pixels.jpg")

#or

np.save("map-red-pixels.jpg", red_image1, allow_pickle=True, fix_imports=True)

#line 10
red_image = np.empty((1053, 1140))




   im = Image.open(map_filename)
    pix = im.load()
    width, height = im.size

    MARK = []
    for i in range(0, 1053):
        MARK.append([])
        for j in range(0, 1140):
            MARK[i].append(0)

    Q = [] #try and change to numpy array later
    WHITE = (255, 255, 255)
    conncomponents = 0

    whitepixels = 0
    for j in range(0, height):
        for i in range(0, width):
            if pix[i, j] == WHITE:
                whitepixels += 1
    print(whitepixels)

    whitepixels = 0

    for j in range(0, height):
        for i in range(0, width):
            regionsize = 0
            if (pix[i, j] == WHITE) and (MARK[i][j] == 0):
                MARK[i][j] = 1
                Q.append((i, j))
                while Q != []:
                    q = Q.pop(0)
                    x = q[0]
                    y = q[1]
                    n = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            n.append((x+i, y+j))
                    n.remove((x, y))

                    regionsize += 1
                    for each in n:
                        if (pix[each[0], each[1]] == WHITE) and (MARK[each[0]][each[1]] == 0):
                            regionsize += 1
                            MARK[each[0]][each[1]] = 1
                            Q.append(each)
                    
                if regionsize >= 2:
                    conncomponents += 1
                    whitepixels += regionsize
                    #print(conncomponents, regionsize)
    
    print(whitepixels)
    


    #for {each pixel in IMG, going through each row left to right}:
        #if {pixel(x, y) is white} and {MARK(x, y) is unvisited}:
            #set {MARK(x, y) to visited}
            #append {pixel(x, y) to Q}
            #while Q != []:
                #remove the first item from Q, set this to q(m, n)
                #for each 8-neighbour n(s, t) of q(m, n):
                    #if n(s, t) is white and MARK(s, t) is unvisited:
                        #set MARK(s, t) to visited
                        #add n(s, t) to Q
    
    #count = 1
    #noconnected = 0
    #for each in MARK
        #if each != 0:
            #write to text file("Connected Component", count, ", number of pixels =", each)
            #noconnected += 1
        #count += 1
    #write to text file("Total number of connected components =", noconnected)

red_image = red_image.transpose(Image.Transpose.ROTATE_270)
    red_image = red_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)