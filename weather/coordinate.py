#!/usr/bin/python3
""" Module contain function to retrieve user coordinate. """

def get_cord():
    """ retrieves coordinates """
    import requests

    coord = {}
    url = 'https://ipwho.is'
    req = requests.get(url).json()
    coord['longitude'] = req['latitude']
    coord['latitude'] = req['latitude']
    coord['region'] = req['region']
    coord['country'] = req['country']
    return coord
