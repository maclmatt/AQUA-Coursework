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