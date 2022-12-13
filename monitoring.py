# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#
import matplotlib.pyplot as plt
import requests
import json
import datetime
from utils import maxvalue
import numpy as np

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    if start_date is None:
        start_date = datetime.date.today()
    if end_date is None:
        end_date = start_date + datetime.timedelta(days=1)
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    return res.json()

def create_graph_multiple_lines(lists: list) -> None:
    """Plots graph using values from the list

    Args:
        lists (list): 3D list, contains a 2D list for each line to plot, 
            each of these contains 2 lists: one for the x-coordinates and one for the y-coordinates
    """

    colors = ['r', 'g', 'b']
    for i in range(0, 3):
        xpoints = np.array(lists[i][0])
        ypoints = np.array(lists[i][1])
        plt.plot(xpoints, ypoints, color=colors[i])
    plt.show()

def create_graph(listofpoints: list) -> None:
    """Plots graph using values from the list

    Args:
        listofpoints (list): 2D list, one list for the x-coordinates and one for the y-coordinates
    """

    xpoints = np.array(listofpoints[0])
    ypoints = np.array(listofpoints[1])
    plt.plot(xpoints, ypoints)
    plt.show()

def day_graph(site_code: str):
    """Retrieves the pollutant levels for the current day and the site code specified for all the pollutants, 
        then calls create_graph_multiple_lines() to create a graph with these values

    Args:
        site_code (str): Site code for the pollutant monitoring station to generate a graph for
    """

    levels = [[[], []], [[], []], [[], []]]
    pollutants = np.array(["NO", "PM10", "PM25"])
    for i in range(0, 3):
        data = get_live_data_from_api(site_code, pollutants[i])
        for each in data['RawAQData']['Data']:
            hour = each['@MeasurementDateGMT']
            value = each['@Value']
            if value == '':
                value = 0
            else:
                value = float(value)
            levels[i][0].append(int(hour[11:13]))
            levels[i][1].append(value)
    create_graph_multiple_lines(levels)

def week_graph(site_code: str):
    """Retrieves the pollutant levels for the previous week and the site code specified for all the pollutants, 
        then calls create_graph_multiple_lines() to create a graph with these values

    Args:
        site_code (str): Site code for the pollutant monitoring station to generate a graph for
    """

    levels = [[[], []], [[], []], [[], []]]
    pollutants = np.array(["NO", "PM10", "PM25"])
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    for i in range(0, 3):
        data = get_live_data_from_api(site_code, pollutants[i], week_ago, today)
        for each in data['RawAQData']['Data']:
            hour = each['@MeasurementDateGMT']
            value = each['@Value']
            if value == '':
                value = 0
            else:
                value = float(value)
            levels[i][0].append(float(hour[8:10] + "." + hour[11:13]))
            levels[i][1].append(value)
    create_graph_multiple_lines(levels)

def month_graph(site_code: str):
    """Retrieves the pollutant levels for the previous month and the site code specified for all the pollutants, 
        then calls create_graph_multiple_lines() to create a graph with these values

    Args:
        site_code (str): Site code for the pollutant monitoring station to generate a graph for
    """

    levels = [[[], []], [[], []], [[], []]]
    pollutants = np.array(["NO", "PM10", "PM25"])
    today = datetime.date.today()
    month_ago = today - datetime.timedelta(days=30)
    for i in range(0, 3):
        data = get_live_data_from_api(site_code, pollutants[i], month_ago, today)
        for each in data['RawAQData']['Data']:
            hour = each['@MeasurementDateGMT']
            value = each['@Value']
            if value == '':
                value = 0
            else:
                value = float(value)
            levels[i][0].append(hour)
            levels[i][1].append(value)
    create_graph_multiple_lines(levels)

def day_graph_pollutant(site_code: str, pollutant: str) -> None:
    """Retrieves the specified pollutant levels for the current day and the site code specified, 
        then calls create_graph_multiple_lines() to create a graph with these values

    Args:
        site_code (str): Site code for the pollutant monitoring station to generate a graph for
        pollutant (str): Pollutant to generate a graph for
    """

    levels = [[], []]
    data = get_live_data_from_api(site_code, pollutant)
    for each in data['RawAQData']['Data']:
        hour = each['@MeasurementDateGMT']
        value = each['@Value']
        if value == '':
            value = 0
        else:
            value = float(value)
        levels[0].append(int(hour[11:13]))
        levels[1].append(value)
    create_graph(levels)

def week_graph_pollutant(site_code: str, pollutant: str) -> None:
    """Retrieves the specified pollutant levels for the previous week and the site code specified, 
        then calls create_graph_multiple_lines() to create a graph with these values

    Args:
        site_code (str): Site code for the pollutant monitoring station to generate a graph for
        pollutant (str): Pollutant to generate a graph for
    """

    levels = [[], []]
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    data = get_live_data_from_api(site_code, pollutant, week_ago, today)
    for each in data['RawAQData']['Data']:
        hour = each['@MeasurementDateGMT']
        value = each['@Value']
        if value == '':
            value = 0
        else:
            value = float(value)
        levels[0].append(float(hour[8:10] + "." + hour[11:13]))
        levels[1].append(value)
    create_graph(levels)

def month_graph_pollutant(site_code: str, pollutant: str) -> None:
    """Retrieves the specified pollutant levels for the previous month and the site code specified, 
        then calls create_graph_multiple_lines() to create a graph with these values

    Args:
        site_code (str): Site code for the pollutant monitoring station to generate a graph for
        pollutant (str): Pollutant to generate a graph for
    """

    levels = [[], []]
    today = datetime.date.today()
    month_ago = today - datetime.timedelta(days=25)
    data = get_live_data_from_api(site_code, pollutant, month_ago, today)
    for each in data['RawAQData']['Data']:
        hour = each['@MeasurementDateGMT']
        value = each['@Value']
        if value == '':
            value = 0
        else:
            value = float(value)
        levels[0].append(hour)
        levels[1].append(value)
    create_graph(levels)

def health_advice(site_code: str) -> list:
    """Gets health advice based on pollution levels for a certain area

    Args:
        site_code (str): site code to get health advice for

    Returns:
        list: the populations described by the api, and the health advice for each of these
    """
    
    BASE_URL = 'http://api.erg.ic.ac.uk/AirQuality'
    health_indices = []
    x = requests.get(BASE_URL + '/Daily/MonitoringIndex/Latest/SiteCode={}/Json'.format(site_code))
    sites = x.json()
    for each in sites['DailyAirQualityIndex']['LocalAuthority']['Site']['Species']:
        health_indices.append(int(each['@AirQualityIndex']))

    top_health_index = health_indices[maxvalue(health_indices)]

    x = requests.get(BASE_URL + '/Information/IndexHealthAdvice/AirQualityIndex={}/Json'.format(top_health_index))
    info = x.json()
    populations = []
    health_advice = []
    for each in info['AirQualityIndexHealthAdvice']['AirQualityBanding']['HealthAdvice']:
        populations.append(each['@Population'])
        health_advice.append(each['@Advice'])

    return populations, health_advice
