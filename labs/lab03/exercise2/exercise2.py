def find_station(stations, name):
    station_number = 0
    for item in stations:
        if item == name:
            return station_number
        station_number += 1
    return -1


def count_stops(stations, start, stop):
    start_index = find_station(stations, start)
    stop_index = find_station(stations, stop)

    if start_index == -1 or stop_index == -1:
        return -1

    return abs(stop_index - start_index)
