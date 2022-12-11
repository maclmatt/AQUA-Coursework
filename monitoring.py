# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#
import matplotlib.pyplot as plt #def will need
import requests
import json

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    print(res)

    #the api docs are here - http://api.erg.ic.ac.uk/AirQuality/help

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

    return res.json()


def rm_function_1(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def rm_function_2(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def rm_function_3(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def rm_function_4(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

get_live_data_from_api()