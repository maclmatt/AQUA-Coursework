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

import requests
import json

GROUP_NAME = 'London'
BASE_URL = 'http://api.erg.ic.ac.uk/AirQuality'

x = requests.get(BASE_URL + '/Information/MonitoringLocalAuthority/GroupName=' + GROUP_NAME + '/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))
authorities = x.json()
for authority in authorities['LocalAuthorities']['LocalAuthority']:
    print(authority['@LocalAuthorityName'])
    print(authority['@LocalAuthorityCode'])

x = requests.get(BASE_URL + '/Information/MonitoringSites/GroupName=' + GROUP_NAME + '/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))
sites = x.json()
for site in sites['Sites']['Site']:
    print(site['@LocalAuthorityName'])
    print(site['@LocalAuthorityCode'])
    print(site['@SiteName'])
    print(site['@SiteCode'])

x = requests.get(BASE_URL + '/Information/Species/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))


x = requests.get(BASE_URL + '/Daily/MonitoringIndex/Latest/LocalAuthorityId=5/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))

x = requests.get(BASE_URL + '/Daily/MonitoringIndex/Latest/SiteCode=BY7/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))

x = requests.get(BASE_URL + '/Information/IndexHealthAdvice/AirQualityIndex=2/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))

x = requests.get(BASE_URL + '/Information/IndexHealthAdvice/AirQualityIndex=5/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))

x = requests.get(BASE_URL + '/Information/IndexHealthAdvice/AirQualityIndex=8/Json')
print (x.status_code) #200 means it all went ok
print (json.dumps(x.json(), indent=4))