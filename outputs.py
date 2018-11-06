# Ivan Wan Le Huang 60062626

# Is this generate function all I should have in each class?
# DO I need to annotate classes along with each function within a class?
# Just to make sure, since we can assume that the user knows the correct format,
# We don't have to prompt user again if inputs are invalid, right?

import mapquest_api


class Steps:

    def generate(self, route_result: dict) -> None:
        '''
        Takes a parsed JSON response from Mapquest's Open Direction's API
        and prints out all the steps for the route from the response
        '''

        print('DIRECTIONS')
        route_data = route_result['route']
        for leg in route_data['legs']:
            for maneuver in leg['maneuvers']:
                print(maneuver['narrative'])
        print()

class TotalDistance:

    def generate(self, route_result: dict) -> None:
        '''
        Takes a parsed JSON response from Mapquest's Open Direction's API
        and prints out the total distance required to travel from the response
        '''
        route_data = route_result['route']
        total_distance = convert_distance(route_data['distance'])
        print('TOTAL DISTANCE: ' + total_distance + ' miles')
        print()

class TotalTime:

    def generate(self, route_result: dict) -> None:
        '''
        Takes a parsed JSON response from Mapquest's Open Direction's API
        and prints out the total time required to travel from the response
        '''

        route_data = route_result['route']
        total_time = route_data['time']
        new_time = convert_sec_min(total_time)
        print('TOTAL TIME: ' + new_time + " minutes")
        print()

class LatLong:

    def generate(self, route_result: dict) -> None:
        '''
        Takes a parsed JSON response from Mapquest's Oenn Direction's API
        and prints out the longitude and latitude of each location
        '''
        print('LATLONGS')
        route_data = route_result['route']
        for location in route_data['locations']:
            location_lng = convert_long(location['latLng']['lng'])
            location_lat = convert_lat(location['latLng']['lat'])
            print(location_lat + " " + location_lng)
        print()

class Elevation:

    def generate(self, route_result: dict) -> None:
        '''
        Takes a parsed JSON response from Mapquest's Open Direction's API
        and uses the latitude and longitude for each location
        '''

        print('ELEVATIONS')
        for location in route_result['route']['locations']:

            latlng_collection = []
            latlng_collection.append(location['latLng']['lat'])
            latlng_collection.append(location['latLng']['lng'])
            elevation_response = mapquest_api.get_elevation_response(latlng_collection)
            for elevation_profile in elevation_response['elevationProfile']:
                location_elevation = elevation_profile['height']
                print(convert_height(location_elevation))
        print()


def convert_distance(distance: float) -> str:
    '''
    Takes an integer (distance from json response) and formats it
    to proper output in miles
    '''

    distance_max = distance + 1
    if distance_max - distance >= 0.5:
        distance_max = distance_max - 1
    new_time = str(round(distance_max))
    return new_time

def convert_sec_min(time: float) -> str :
    '''
    takes an integer (time from json response) and formats it
    to proper output in minutes
    '''

    total_time = time / 60
    total_time_min = time // 60
    if total_time - total_time_min >= 0.5:
        total_time_min = total_time_min + 1
    new_time = str(total_time_min)
    return new_time


def convert_lat(lat: int) -> str:
    '''Takes an integer (latitude from json response) and formats it
    into proper output form
    '''

    lat_string = '%.2f' % (lat)
    if lat >= 0:
        return lat_string + "N"
    elif lat < 0:
        len_str = len(lat_string)
        lat_string = lat_string[1:len_str]
        return lat_string + "S"
    else:
        return lat_string

def convert_long(long: int) -> str:
    '''
    Takes an integer (longitude from json response) and formats it
    into proper output form
    '''

    long_string = '%.2f' % (long)
    if long > 0:
        return long_string + "E"
    elif long == 0:
        return long_string + "W"
    elif long < 0:
        len_str = len(long_string)
        long_string = long_string[1:len_str]
        return long_string + "W"
    else:
        return long_string

def convert_height(height: int) -> str:
    '''
    Takes an integer (height from json response) and formats it
    to proper output in feet
    '''

    new_height = height * 3.28084
    new_height = '%.0f' % (new_height)
    return new_height

