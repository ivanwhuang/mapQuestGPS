# Ivan Wan Le Huang 60062626
import mapquest_api
import outputs

def find_desired_locations() -> list:
    '''
    Finds how many locations to route along with the name of
    each location by input. Returns a list of each location in the order
    it was was received.
    '''

    num_trips = input().strip()
    num_trips = int(num_trips)
    location_list = []
    for num in range(num_trips):
        location = input()
        location_list.append(location)
    return location_list

def find_outputs() -> list:
    '''
    Asks how many outputs and which outputs the user wants.
    For each output desired by the user, an object of the respective output class is constructed and stored into
    a list. This function returns that list of output objects
    '''

    num_outputs = input()
    num_outputs = int(num_outputs)

    output_dict = dict()
    output_dict['STEPS'] = outputs.Steps()
    output_dict['TOTALDISTANCE'] = outputs.TotalDistance()
    output_dict['TOTALTIME'] = outputs.TotalTime()
    output_dict['LATLONG'] = outputs.LatLong()
    output_dict['ELEVATION'] = outputs.Elevation()

    output_list = []
    for num in range(num_outputs):
        output = input()
        output_list.append(output_dict[output])

    return output_list


def output_generate(output_list: list, api_route_response: dict) -> None:
    '''For each output object desired by the user, object searches through an api response and displays
       information based on the specified output
    '''

    for output in output_list:
        output.generate(api_route_response)



if __name__ == '__main__':
    desired_locations = find_desired_locations()
    desired_outputs = find_outputs()

    try:
        route_response = mapquest_api.get_route_response(desired_locations)
        if mapquest_api.check_route_error(route_response) == True:
            print()
            output_generate(desired_outputs, route_response)
            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    except:
        print("\n" + "MAPQUEST ERROR")






