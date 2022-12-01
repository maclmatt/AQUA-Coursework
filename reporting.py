import numpy as np
import csv
import datetime
from utils import sumvalues, meannvalue, countvalue


def daily_average(data: str, monitoring_station: str, pollutant: str) -> list: #DONE 4 marks
    """Calculates daily averages for a pollutant at a monitoring station

    Args:
        data (str): subdirectory of monitoring_station csv file
        monitoring_station (str): csv file name for the monitoring station to find daily averages for
        pollutant (str): pollutant to find daily averages for

    Returns:
        list: daily averages of pollutant at monitoring station
    """
    
    if pollutant == "NO":
        pollutantindex = 2
    elif pollutant == "PM10":
        pollutantindex = 3
    elif pollutant == "PM2.5":
        pollutantindex = 4
    with open(data + monitoring_station) as csv_file:
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
            nodata = False
            while count < 24:
                try:
                    pollutantvalues.append(float(rows[line_count][pollutantindex]))
                except:
                    nodata = True
                line_count += 1
                count += 1
            if nodata:
                daily_averages.append("Incomplete data")
            else:
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
    with open(data + monitoring_station) as csv_file:
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
            nodata = False
            while count < 24:
                try:
                    pollutantvalues.append(float(rows[line_count][pollutantindex]))
                except:
                    nodata = True
                line_count += 1
                count += 1
            if nodata:
                daily_medians.append("Incomplete data")
            else:
                pollutantvalues.sort()
                median = (pollutantvalues[12] + pollutantvalues[11])/2
                daily_medians.append(median)
            daycount += 1
    return daily_medians
    
def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def peak_hour_date(data, date, monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

def count_missing_data(data,  monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
