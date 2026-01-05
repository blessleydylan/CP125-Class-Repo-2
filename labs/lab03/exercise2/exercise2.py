def find_station(stations, name):
    station_number = 0
    for item in stations:
        if item == name:
            return station_number
        station_number += 1
    return None


def count_stops(stations, start, stop):
    station_number = 0
    station_number2 = 0

    # find start position
    for item in stations:
        if item == start:
            break
        station_number += 1
    else:
        return -1   # start not found

    # find stop position
    for item2 in stations:
        if item2 == stop:
            break
        station_number2 += 1
    else:
        return -1   # stop not found

    # calculate stops
    if station_number > station_number2:
        return station_number - station_number2
    else:
        return station_number2 - station_number
