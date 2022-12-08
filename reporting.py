import numpy as np
import csv
import datetime
from utils import sumvalues, meannvalue, countvalue, maxvalue

#DELETE AT SOME POINT: executive decision made to just not append anything when 'no data' is encountered


def daily_average(data: str, monitoring_station: str, pollutant: str) -> list: #DONE 4 marks
    """Calculates daily averages for a pollutant at a monitoring station

    Args:
        data (str): subdirectory of monitoring_station csv file
        monitoring_station (str): csv file name for the monitoring station to find daily averages for
        pollutant (str): pollutant to find daily averages for

    Returns:
        list: daily averages of pollutant at monitoring station
    """
    
    if pollutant == "no":
        pollutantindex = 2
    elif pollutant == "pm10":
        pollutantindex = 3
    elif pollutant == "pm25":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        for row in csv_reader:
            rows.append(row)
        daily_averages = []
        line_count = 1
        daycount = 0
        while daycount < 365:
            count = 0
            pollutantvalues = []
            while count < 24:
                try:
                    pollutantvalues.append(float(rows[line_count][pollutantindex]))
                    line_count += 1
                    count += 1
                except:
                    line_count += 1
                    count += 1
            daily_averages.append(meannvalue(pollutantvalues))
            daycount += 1
    return daily_averages

def daily_median(data: str, monitoring_station: str, pollutant: str) -> list: #DONE 5 marks
    """Calculates daily medians for a pollutant at a monitoring station

    Args:
        data (str): subdirectory of monitoring_station csv file
        monitoring_station (str): csv file name for the monitoring station to find daily medians for
        pollutant (str): pollutant to find daily medians for

    Returns:
        list: daily medians of pollutant at monitoring station
    """

    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        for row in csv_reader:
            rows.append(row)
        daily_medians = []
        line_count = 1
        daycount = 0
        while daycount < 365:
            count = 0
            pollutantvalues = []
            while count < 24:
                try:
                    pollutantvalues.append(float(rows[line_count][pollutantindex]))
                    line_count += 1
                    count += 1
                except:
                    line_count += 1
                    count += 1
            pollutantvalues.sort()
            valuescount = len(pollutantvalues)
            if valuescount%2 == 0:
                median = (pollutantvalues[int(valuescount/2)] + pollutantvalues[int(valuescount/2)-1])/2
            elif valuescount == 1:
                median = pollutantvalues[0]
            else:
                median = pollutantvalues[(valuescount//2)+1]
            daily_medians.append(median)
            daycount += 1
    return daily_medians
    
def hourly_average(data: str, monitoring_station: str, pollutant: str) -> list: #DONE 5 marks
    """Calculates hourly averages across 365 days for a particular pollutant and monitoring station

    Args:
        data (str): subdirectory of monitoring_station csv file
        monitoring_station (str): csv file name for the monitoring station to find hourly averages for
        pollutant (str): pollutant to find hourly averages for

    Returns:
        list: list of hourly averages for particular pollutant and monitoring station
    """
    
    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        for row in csv_reader:
            rows.append(row)
        lists = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        day_count = 0
        line_count = 1
        while day_count < 365:
            for each in lists:
                try:
                    each.append(float(rows[line_count][pollutantindex]))
                    line_count += 1
                except:
                    line_count += 1
            day_count += 1
        hourly_averages = []
        for each in lists:
            try:
                hourly_averages.append(meannvalue(each))
            except:
                hourly_averages.append("Incomplete data")
        return hourly_averages

def monthly_average(data: str, monitoring_station: str, pollutant: str) -> list: #DONE 4 marks
    """Calculates the montly average of a pollutant at a particular monitoring station

    Args:
        data (str): subdirectory of monitoring_station csv file
        monitoring_station (str): csv file name for the monitoring station to find monthly averages for
        pollutant (str): pollutant to find monthly averages for

    Returns:
        list: list of monthly averages for particular monitoring station and pollutant
    """
    
    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dates = []
        pollutantvalues = []
        for row in csv_reader:
            dates.append(row[0])
            pollutantvalues.append(row[pollutantindex])
        monthly_averages = []
        line_count = 1
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        datem = datetime.datetime.strptime(dates[line_count], "%Y-%m-%d")
        for each in months:
            monthvalues = []
            while (datem.month == each) and (line_count < 8760):
                try:
                    monthvalues.append(float(pollutantvalues[line_count]))
                    line_count += 1
                    datem = datetime.datetime.strptime(dates[line_count], "%Y-%m-%d")
                except:
                    line_count += 1
                    datem = datetime.datetime.strptime(dates[line_count], "%Y-%m-%d")
            monthly_averages.append(meannvalue(monthvalues))
        return monthly_averages

def peak_hour_date(data: str, date: str, monitoring_station: str, pollutant: str) -> str: #DONE 4 marks
    """Finds the hour with the highest pollution of the pollutant on a particular date for a particular monitoring station

    Args:
        data (str): subdirectory of monitoring_station csv file
        date (str): date to find peak hour for
        monitoring_station (str): csv file name for the monitoring station to find peak hour for
        pollutant (str): pollutant to find peak hour for

    Returns:
        str: hour in 24-hr clock that has the peak amount of pollutant for the particular date and monitoring station
    """
    
    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dates = []
        pollutantvalues = []
        for row in csv_reader:
            dates.append(row[0])
            pollutantvalues.append(row[pollutantindex])
        datesvalues = []
        for line_count in range(1, 8761):
            datem = datetime.datetime.strptime(dates[line_count], "%Y-%m-%d")
            if str(datem.date()) == date:
                try:
                    datesvalues.append(float(pollutantvalues[line_count]))
                except:
                    line_count += 1
                    line_count -= 1
        peakvalueindex = maxvalue(datesvalues)
        peakhour = peakvalueindex + 1
        return peakhour
        
def count_missing_data(data: str, monitoring_station: str, pollutant: str) -> int: #DONE 4 marks
    """Calculates number of 'No data' entries in the data for a particular monitoring station and pollutant

    Args:
        data (str): subdirectory of monitoring_station csv file
        monitoring_station (str): csv file name for the monitoring station to count the missing data for
        pollutant (str): pollutant to count the missing data for

    Returns:
        int: number of 'No data' entries that are in the data
    """
    
    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        for row in csv_reader:
            rows.append(row[pollutantindex])
        arr = np.array(rows)
        nodatacount = 0
        x = np.where(arr == 'No data')
        nodatacount = len(x[0])
    return nodatacount

def fill_missing_data(data: str, new_value: float,  monitoring_station: str, pollutant: str) -> list: #DONE 4 marks
    """Returns copy of the data for a monitoring station, with all the 'No data' entries for a 
        particular pollutant replaced with a new value

    Args:
        data (str): subdirectory of monitoring_station csv file
        new_value (float): new value to replace the 'No data' entries
        monitoring_station (str): csv file name for the monitoring station to fill the missing data for
        pollutant (str): pollutant to fill the missing data for

    Returns:
        list: copy of the data for the monitoring station with new values relacing 'No data' entries
    """
    
    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    if monitoring_station == "HRL":
        monitoring_station = "data/Pollution-London Harlington.csv"
    elif monitoring_station == "MY1":
        monitoring_station = "data/Pollution-London Marylebone Road.csv"
    elif monitoring_station == "KC1":
        monitoring_station = "data/Pollution-London N Kensington.csv"
    with open(monitoring_station) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        for row in csv_reader:
            rows.append(row)
        arr = np.array(rows)
        for each in arr:
            if each[pollutantindex] == 'No data':
                each[pollutantindex] = new_value
        return arr
