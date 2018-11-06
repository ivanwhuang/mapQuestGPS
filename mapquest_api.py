# Ivan Wan Le Huang 60062626

import json
import urllib.parse
import urllib.request

BASE_MAPQUEST_ROUTE_URL = 'http://open.mapquestapi.com/directions/v2'
BASE_MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'
MAPQUEST_API_KEY = 'JK3V4iiYpabyAXG1EFvxitt5KAunGFEL'


def build_route_url(location_query: list) -> str:
    '''
    Takes a location query and uses it to build and returns
    a URL that can be used to ask the Directions API
    to gain any information in regards to the route to each location
    '''
    query_parameters = [
        ('key', MAPQUEST_API_KEY)
    ]
    num_locations = len(location_query)

    from_location_query = ('from', location_query[0])
    query_parameters.append(from_location_query)
    counter = 1
    while counter < num_locations:
        to_location_query = ('to', location_query[counter])
        query_parameters.append(to_location_query)
        counter += 1

    return BASE_MAPQUEST_ROUTE_URL + '/route?' + urllib.parse.urlencode(query_parameters)


def build_elevation_url(latlng_query: list) -> str:
    '''
    Takes a location query and uses it to build and returns
    a URL that can be used to ask the Elevations API
    to gain any information in regards to the elevation of each location
    '''

    query_parameters = [('key',MAPQUEST_API_KEY), ('shapeFormat', 'raw')]

    len_latlng = len(latlng_query)
    latlng_parameter = '&latLngCollection='

    for counter in range(len_latlng):
        if counter < len_latlng - 1:
            latlng_parameter = latlng_parameter + str(latlng_query[counter]) + ','
        else:
            latlng_parameter = latlng_parameter + str(latlng_query[counter])

    return BASE_MAPQUEST_ELEVATION_URL + '/profile?' + urllib.parse.urlencode(query_parameters) + latlng_parameter


def get_response(url: str) -> dict:
    '''
    Takes a URL and returns a Python Dictionary representing
    the parsed json response
    '''

    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)

    finally:
        if response != None:
            response.close()

def check_route_error(api_response: dict) -> bool:
    '''
    Checks if each desired location can be routed by MapQuest.
    Returns True if MapQuest can route each location.
    Returns False and prints "NO ROUTE FOUND" if invalid location.
    Returns False and prints "MAPQUEST ERROR" if some other error took place.
    '''

    info = api_response['info']
    if info['statuscode'] == 0:
        return True
    elif info['statuscode'] == 402:
        print("\n" + "NO ROUTE FOUND")
        return False
    else:
        print()
        print("\n" + "MAPQUEST ERROR")
        return False

def get_route_response(locations: list) -> dict:
    '''
    Uses the desired locations to finds the Python Dictionary
    that represents the parsed json response given by the Directions API
    '''

    url = build_route_url(locations)
    print(url)
    api_response = get_response(url)
    return api_response

def get_elevation_response(latlngs: list) -> dict:
    '''
    Uses the desired latitude and longitudes to find the Python Dictionary
    that represents the parsed json response given by the Directions API
    '''

    url = build_elevation_url(latlngs)
    api_response = get_response(url)
    return api_response
