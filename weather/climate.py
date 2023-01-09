#!/usr/bin/python3
""" Retrieves weather information. """
import requests
from os import getenv

def current(lon, lat):
    """ fetch current weather data """
    headers = {'User-Agent': 'SEAJRO_WEATHER_APP'}
    api_key = getenv('SEAJRO_WEATHER_API')
    url = 'https://api.weatherbit.io/v2.0/current'
    params = {'lat': lat, 'lon': lon, 'key': api_key}
    req = requests.get(url, params=params).json()
    return req

def forecast(city, country, days):
    """fetches weather forecast
    params:
            days:    number of forecast days to fetch
            country: country to query weather data for
            city:    city to query weather data for
    """
    api_key = getenv('SEAJRO_API')
    url = 'https://api.weatherbit.io/v2.0/forecast/daily'
    params = {'city': city, 'country': country, 'days': days}
    req = requests.get(url, params=params).json()
    req = req['data']
    return req
