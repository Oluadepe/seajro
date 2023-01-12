#!/usr/bin/python3
""" Retrieves weather information. """
import requests
from os import getenv

def current(lon, lat):
    """ fetch current weather data """
    headers = {'User-Agent': 'SEAJRO_WEATHER_APP'}
    api_key = getenv('SEAJRO_WEATHER_API')
    url = getenv('SEAJRO_CURRENT_URL')
    params = {'lat': lat, 'lon': lon, 'key': api_key}
    req = requests.get(url, params=params).json()
    dict_ = {}
    dict_['description'] = req['data'][0]['weather']['description'] + '.'
    dict_['city_name'] = req['data'][0]['city_name']
    dict_['country_code'] = req['data'][0]['country_code']
    dict_['temp'] = req['data'][0]['temp']
    return dict_

def forecast(city, country, days):
    """fetches weather forecast
    params:
            days:    number of forecast days to fetch
            country: country to query weather data for
            city:    city to query weather data for
    """
    api_key = getenv('SEAJRO_API')
    url = getenv('SEAJRO_FORECAST_URL')
    params = {'city': city, 'country': country, 'days': days}
    req = requests.get(url, params=params).json()
    req = req['data']
    return req
