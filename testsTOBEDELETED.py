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


list1 = [22.453, 19.099, 20.925, 19.974, 17.363, 12.434, 13.316,13.335,16.811,19.01,21.757,22.738,24.545,27.694,25.764,22.068,22.229,20.708,19.385,16.995,14.024,11.314,7.723,6.831]
list1.sort()
print(list1)